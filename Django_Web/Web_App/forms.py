from django import forms
from django.forms import ModelForm
from django.core import validators
from .models import Customer


class RegisterForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=('first_name', 'last_name', 'email_address', 'password', 'confirm_password')


class LoginForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=('username', 'email_address', 'password')
