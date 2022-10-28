from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    phone=forms.CharField(max_length=12)
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','phone','password1','password2']