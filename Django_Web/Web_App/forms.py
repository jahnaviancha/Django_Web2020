from django import forms
from django.forms import ModelForm
from django.core import validators
from .models import Student


class signup_form(forms.ModelForm):
    class Meta:
        model=Student
        fields = "__all__"


class LoginForm(forms.ModelForm):
    class Meta:
        model=Student
        fields= "__all__"
