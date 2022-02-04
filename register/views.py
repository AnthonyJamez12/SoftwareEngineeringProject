from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect


# Create your views here.

def register(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        new_user = form.save()
        messages.info(request, "Thanks for registering. You are now logged in.")
        new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        login(request, new_user)
        return HttpResponseRedirect("/")
    else:
        form = RegisterForm()


    return render(request, "register/register.html", {"form": form})


def logout(request):
    auth.logout(request)
    return redirect('/register')
