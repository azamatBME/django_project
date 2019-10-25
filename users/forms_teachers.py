from django import forms
from django.contrib.auth.models import User
from .models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    subject = forms.CharField(
        label='Subject',
        widget=forms.TextInput(attrs={'placeholder': 'Arts'})
    )
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(attrs={'placeholder': 'Associate Professor'})
    )


class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2','subject','title']
