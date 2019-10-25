from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    major = forms.CharField(
        label='Major',
        widget=forms.TextInput(attrs={'placeholder': 'Electrical engineering'})
    )


class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2','address_1','major']

