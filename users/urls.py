from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'), # The LoginView class handles authentication, and the two arguments tell Django which template to use and what URL to use for the login view.
    path('logout/', views.logout_view, name='logout'), # The logout_view() function is our own view for logging out a user. We'll create the view in the users app, and we'll use the name 'logout' so we can refer to it in our code.
    path('register/', views.register, name='register'), # The register view is our own view, which we'll write soon. We use the name 'register' so we can refer to it in our code.
]

# The first path() function includes the default auth URLs. The second argument tells Django to use the default auth views. The third argument gives the URL a name that we can use to refer to it in our code; this name is similar to the names we've been using for our own URLs, so it's important to be consistent.