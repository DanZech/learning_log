# URL project: http://localhost:8000/
from django.contrib import admin # importa o modulo admin
from django.urls import path, include # importa o modulo path e include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('', include(('learning_logs.urls', 'learning_logs'), namespace='learning_logs')),
]
