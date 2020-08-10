from django import forms
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import RegisterForm,LoginForm
from django.contrib.auth import authenticate
from . import models


# Create your views here.

def home(request):
    if request.method == 'POST':
        form= RegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('login')
            except:
                pass
    else:
        form=RegisterForm()
    return render(request, 'home.html', {'form': form})


def success(request):
    return render(request, 'success.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_vaild():
            form.save()
            return redirect('success')
        else:
            pass
    else:
        form = LoginForm()
    return render(request, 'login.html', {' form':form})
