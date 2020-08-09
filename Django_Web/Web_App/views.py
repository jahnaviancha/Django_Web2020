from django import forms
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from . import forms
from . import models


# Create your views here.

def home(request):
    if request.method == 'POST':
        form=forms.signup_form(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('login')
            except:
                pass
    else:
        form=forms.signup_form()
    return render(request, 'home.html', {'form': form})


def success(request):
    return render(request, 'success.html')


def login(request):
    if request.method == 'POST':
        form=forms.LoginForm(request.POST)
        if form.is_vaild():
            try:
                form.save()
                return redirect('success')
            except:
                pass
    return render(request, 'login.html', {'form': form})
