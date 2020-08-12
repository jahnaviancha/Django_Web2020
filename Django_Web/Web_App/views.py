from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User


# Create your views here.


def signup(request):
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form=RegisterForm()
    return render(request, 'home.html', {'form': form})


def success(request):
    return render(request, 'success.html')


def user_login(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect('success')
    else:
        form=LoginForm()
    return render(request, 'login.html',{'form': form})
