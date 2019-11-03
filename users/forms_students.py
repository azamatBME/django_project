from django import forms
from .models import User
from .models import Student
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    address = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    major = forms.CharField(
        label='Major',
        widget=forms.TextInput(attrs={'placeholder': 'Electrical engineering'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'address', 'major']

    @transaction.atomic
    def save(self):
        user = get_user_model()
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        address = self.cleaned_data['address']
        major = self.cleaned_data['major']
        student = Student.objects.create(user=user, address=address, major=major)
        return student
