from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from django.forms import ModelForm
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=30)
    username=forms.CharField(max_length=35)
    email=forms.EmailField(max_length=50)
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('first_name', 'last_name', 'username', 'email', 'password', 'confirm_password')

    def clean_confirm_password(self):
        password=self.cleaned_data.get('password')
        confirm_password=self.cleaned_data.get('confirm_password')
        print(password)
        print(confirm_password)
        if password != confirm_password:
            raise forms.ValidationError("Password not match")
        return confirm_password


class LoginForm(forms.Form):
    username=forms.CharField(max_length=50, required=True)
    password=forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model=User
        fields=('username', 'password')

    # def clean(self):
    #     username=self.cleaned_data.get('username')
    #     password=self.cleaned_data.get('password1')
    #     if username and password:
    #         user=authenticate(username=username, password=password)
    #         if not user or not user.is_active:
    #             raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
    #         if not user.check_password(password):
    #             raise forms.ValidationError("Incorrect password")
