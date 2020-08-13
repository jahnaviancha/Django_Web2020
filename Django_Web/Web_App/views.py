from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegisterForm, LoginForm, StudentCreate

# Create your views here.
from .models import Student, Class


def signup(request):
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form=RegisterForm()
    return render(request, 'home.html', {'form': form})


def details(request):
    if request.method == "POST":
        form=StudentCreate(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('success')
            except:
                pass
    else:
        form=StudentCreate()
    return render(request, 'blog.html', {'form': form})


def success(request):
    context=Class.objects.all()
    return render(request, 'show.html', {'context': context})


def edit(request, id):
    context=Class.objects.get(id=id)
    return render(request, 'edit.html', {'context': context})


def update(request, id):
    context=Class.objects.get(id=id)
    form=StudentCreate(request.POST)
    if form.is_valid():
        form.save()
        return redirect('success')
    return render(request, 'edit.html', {'context': context})


def destroy(request, id):
    context=Class.objects.get(id=id)
    context.delete()
    return redirect('success')


def user_login(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            return redirect('details')
    else:
        form=LoginForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    if request.method == 'POST':
        logout(request)
    return redirect('user_login')


def about(request):
    return render(request, 'about.html')




