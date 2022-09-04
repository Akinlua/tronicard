
from django import forms
from django.forms import ModelForm
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model= User
        fields=['first_name', 'email', 'username', 'password1', 'password2']
        labels={
            'first_name':'Name'
        }

class ProfileForm(ModelForm):
    class Meta:
        model= Profile
        fields= ['name','email', 'username']