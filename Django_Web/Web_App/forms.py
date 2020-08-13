from django import forms

from .models import Student, Class


class RegisterForm(forms.ModelForm):
    email=forms.EmailField(max_length=50, widget=forms.EmailInput)
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=Student
        fields=('first_name', 'last_name', 'username', 'email', 'password', 'confirm_password')

    def clean_confirm_password(self):
        password=self.cleaned_data.get('password')
        confirm_password=self.cleaned_data.get('confirm_password')
        if not password == confirm_password:
            raise forms.ValidationError("Password not match")
        return confirm_password

    def clean_username(self):
        username=self.cleaned_data.get('username')
        check_username=Student.objects.filter(username=username).exists()
        if check_username:
            raise forms.ValidationError("User name already exist")
        return username

    def clean_email(self):
        email=self.cleaned_data.get('email')
        check_email=Student.objects.filter(email=email).exists()
        if check_email:
            raise forms.ValidationError("Email name already exist")
        return email


class LoginForm(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')
        check_username=Student.objects.filter(username=username).exists()
        check_password=Student.objects.filter(password=password).exists()
        if check_username == check_password:
            print("Login Success")
        else:
            raise forms.ValidationError('Check password and username')


class StudentCreate(forms.ModelForm):
    class Meta:
        model=Class
        fields="__all__"
