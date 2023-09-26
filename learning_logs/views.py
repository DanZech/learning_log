from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required # o decorador login_required verifica se o usuário está logado 
from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    """a página inicial de Learning Log"""
    return render(request, 'learning_logs/index.html')

@login_required # o decorador login_required verifica se o usuário está logado antes de executar a função new_topic()
def topics(request):
    """mostra todos os assuntos"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added') # o método filter() retorna um conjunto de objetos do tipo Topic, ordenados de acordo com o atributo date_added. O argumento owner=request.user diz ao Django para buscar somente os tópicos cujo atributo owner seja igual ao usuário atual. O atributo owner é uma instância de User, que significa que cada instância de Topic está associada a uma instância específica de User. Quando um usuário é excluído, todas as instâncias de Topic associadas a esse usuário também serão excluídas.
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required # o decorador login_required verifica se o usuário está logado antes de executar a função topic()
def topic(request, topic_id):
    """mostra um único assunto e todas as suas entradas"""
    topic = Topic.objects.get(id=topic_id) # o método get() recebe como argumento o valor de um atributo, ou um conjunto de atributos, que correspondem a um registro no banco de dados
    # Verifica se o assunto pertence ao usuário atual
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added') # o sinal de menos na frente de date_added classifica os resultados em ordem inversa, para que as entradas mais recentes sejam exibidas primeiro
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)



@login_required # o decorador login_required verifica se o usuário está logado antes de executar a função new_topic()
def new_topic(request):
    """adiciona um novo assunto"""
    if request.method != 'POST': # se o método for diferente de POST, significa que o usuário ainda não submeteu seus dados
        # Nenhum dado de submissão; cria um formulário em branco
        form = TopicForm()
    else:
        # Dados de POST submetidos; processa os dados
        form = TopicForm(request.POST) # cria uma instância de TopicForm e armazena-a em form
        if form.is_valid(): # verifica se o usuário preencheu todos os campos do formulário e não deixou nenhum em branco
            new_topic = form.save(commit=False) # cria um novo objeto Topic e armazena-o em new_topic sem salvá-lo no banco de dados ainda
            new_topic.owner = request.user # define o atributo owner de new_topic como o usuário atual
            new_topic.save() # salva os dados no banco de dados
            return HttpResponseRedirect(reverse('learning_logs:topics')) # redireciona o usuário para a página topics
        
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)



@login_required # o decorador login_required verifica se o usuário está logado antes de executar a função new_entry()
def new_entry(request, topic_id):
    '''adiciona uma nova entrada para um assunto em particular'''
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST': # se o método for diferente de POST, significa que o usuário ainda não submeteu seus dados
        # Nenhum dado de submissão; cria um formulário em branco
        form = EntryForm()

    else:
        # Dados de POST submetidos; processa os dados
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id])) # redireciona o usuário para a página topic
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required # o decorador login_required verifica se o usuário está logado antes de executar a função edit_entry()
def edit_entry(request, entry_id):
    '''edita uma entrada existente'''
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if topic.owner != request.user:
        raise Http404
    
    if request.method != 'POST': # se o método for diferente de POST, significa que o usuário ainda não submeteu seus dados
        # Requisição inicial; preenche previamente o formulário com a entrada atual
        form = EntryForm(instance=entry)
    else:
        # Dados de POST submetidos; processa os dados
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id])) # redireciona o usuário para a página topic
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
