from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm


def logout_view(request):
    """Log the user out."""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        # The first time the register page is requested, the method is GET, so we display a blank registration form. When the form is submitted (method POST), we'll validate the data and create a new user if all is well.
        form = UserCreationForm()
    else:
        # Process completed form.
        # If the method is POST, we create a UserCreationForm instance based on the submitted data. We then call is_valid() to make sure all required fields are filled out (all fields in a UserCreationForm are required). We also check that the two provided passwords match. If the form is valid, we call save(), which stores the username and an encrypted password in the database. The method save() returns the newly created user object, which we store in new_user. We then call authenticate(), passing the username and password to make sure the information matches a user in the database. The authenticate() function returns a boolean value True if the information is valid for a user in the database, and False otherwise. If the information is valid, we use the function login() to redirect the user to the home page.
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
            
    context = {'form': form}
    return render(request, 'users/register.html', context)