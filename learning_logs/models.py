from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """um assunto sobre o qual o usuário está aprendendo"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE) # define uma relação entre os modelos Topic e User, dizendo ao Django que cada instância de Topic está associada a uma instância específica de User. Quando um usuário é excluído, todas as instâncias de Topic associadas a esse usuário também serão excluídas. O argumento on_delete=models.CASCADE diz ao Django para excluir todas as instâncias de Topic quando o usuário for excluído. O atributo owner é uma ForeignKey, uma conexão entre cada tópico e um usuário. Cada usuário é associado a um ID, um número exclusivo atribuído a um usuário quando ele é criado. Quando precisarmos acessar informações associadas a um usuário específico, usaremos o ID. O Django usa esse ID para estabelecer uma conexão entre cada usuário e as informações associadas a ele. O atributo ForeignKey é um código que faz referência a outro registro do banco de dados. O argumento on_delete=models.CASCADE diz ao Django que, quando um usuário é excluído, todas as entradas associadas a esse usuário também devem ser excluídas. O atributo owner é uma instância de User, que significa que cada instância de Topic está associada a uma instância específica de User. Quando um usuário é excluído, todas as instâncias de Topic associadas a esse usuário também serão excluídas.
    
    def __str__(self):
        """devolve uma representação em string do modelo"""
        return self.text
    
class Entry(models.Model):
    """algo específico aprendido sobre um assunto"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        # atribui um nome plural a entry
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """devolve uma representação em string do modelo"""
        return f"{self.text[:50]}..."
 
    '''
    A classe Model é uma classe do Django que fornece a funcionalidade básica para a criação de modelos de banco de dados. Ao herdar da classe Model, a classe Topic ganha a capacidade de ser salva no banco de dados e ter seus atributos acessados e modificados por meio de consultas ao banco de dados. Além disso, a classe Model fornece métodos úteis para a criação de consultas, como objects.all() para obter todos os objetos do modelo e objects.get() para obter um objeto específico com base em um critério de pesquisa.
    '''

    '''
    What are some examples of attributes that can be accessed and modified in a Django model?
    
        In a Django model, attributes are represented as fields. Some examples of fields that can be accessed and modified in a Django model include:

        > CharField: a field for storing character strings
        > IntegerField: a field for storing integers
        > BooleanField: a field for storing boolean values
        > DateField: a field for storing dates
        > DateTimeField: a field for storing date and time values
        > ForeignKey: a field for establishing a many-to-one relationship with another model
        
        These are just a few examples of the types of fields that can be used in a Django model. There are many other types of fields available, and you can also create your own custom fields if needed. For more information on the types of fields available in Django, see the Django documentation on model field reference.
    '''

    '''
    What is the purpose of the objects attribute in a Django model?
    
        The objects attribute in a Django model provides a manager object that allows you to perform database queries on the model. The manager provides methods such as all(), filter(), and get() that allow you to retrieve objects from the database that match certain criteria.

        For example, you can use objects.all() to retrieve all objects of a particular model from the database, or objects.filter() to retrieve a subset of objects that match a specific set of conditions. You can also use objects.get() to retrieve a single object that matches a specific set of conditions.

        The objects attribute is automatically created by Django when you define a model, so you don't need to create it yourself. However, you can create your own custom managers if you need to perform more complex queries on your models.
    
    '''
    '''
    What is a custom manager in Django?
    
        In Django, a custom manager is a way to define custom methods for querying a model's database table. By default, Django provides a manager called objects that provides a set of methods for querying the database. However, you can define your own custom manager to provide additional methods or override the default manager's behavior.

        To define a custom manager, you create a new class that inherits from models.Manager. You can then define methods on this class that perform custom queries on the model's database table. For example, you might define a method that retrieves all topics that were added in the last week.

        Once you have defined your custom manager, you can attach it to your model by adding a objects attribute to your model class that references your custom manager. For example:

                class Topic(models.Model):
                    # fields go here

                    objects = CustomManager()

        In this example, CustomManager is the class that defines your custom manager. Once you have attached your custom manager to your model, you can use its methods to query the model's database table in addition to the methods provided by the default objects manager.

    '''