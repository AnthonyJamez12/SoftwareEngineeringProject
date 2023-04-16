from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register/register.html', {'form': form})

class MyLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True





def logout(request):
    auth.logout(request)
    return redirect('/register')