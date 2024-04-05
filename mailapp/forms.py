from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm 


class RegistrationForm(UserCreationForm):
    email = forms.CharField(label="Email", widget=forms.EmailInput(attrs={"class": "form-control", 
                                                           "placeholder": "Enter your email"}))
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={"class": "form-control",
                                                            "placeholder": "Enter your username"}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control", 
                                                                  "placeholder": "Enter Password"}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={"class": "form-control", 
                                                                  "placeholder": "Re-Enter Password"}))
    class Meta:
        model = User 
        fields = ["email", "username", "password1", "password2"]