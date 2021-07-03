from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "input",
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "input",
    }))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def clean_username(self):
        data = self.cleaned_data['username']
        return data.lower()


class LoginForm(AuthenticationForm):
 
    class Meta:
        model = User
        fields = ['username', 'password']

    def clean_username(self):
        data = self.cleaned_data['username']
        return data.lower()
