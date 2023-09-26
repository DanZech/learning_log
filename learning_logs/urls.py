''' define padroes de URL para learning_logs'''
from django.urls import path # importa a função path, que será usada para definir padrões de URL
from . import views # importa o módulo views do app atual (ponto) que indica o diretório atual

app_name = 'learning_logs'
urlpatterns = [
    # página inicial

    # o padrão de URL vazio corresponde a http://localhost:8000/, que é a página inicial do site
    path('', views.index, name='index'), 

    # o padrão de URL topics/ corresponde a http://localhost:8000/topics/, que é a página que mostra todos os assuntos
    path('topics/', views.topics, name='topics'), 

     # <int:topic_id> é um argumento de URL que corresponde a um número inteiro e o armazena na variável topic_id
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # o padrão de URL new_topic/ corresponde a http://localhost:8000/new_topic/, que é a página para adicionar um novo assunto
    path('new_topic/', views.new_topic, name='new_topic'), 

    # o padrão de URL new_entry/ corresponde a http://localhost:8000/new_entry/, que é a página para adicionar uma nova entrada
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'), 

    # o padrão de URL edit_entry/ corresponde a http://localhost:8000/edit_entry/, que é a página para editar uma entrada
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'), 
]