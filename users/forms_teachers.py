from django import forms
from django.contrib.auth.models import User
from django.db import transaction
from .models import User
from .models import Teacher
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


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

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','first_name', 'last_name',  'email', 'password1',  'password2', 'subject', 'title']

    @transaction.atomic
    def save(self):
        user = get_user_model()
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        subject = self.cleaned_data['subject']
        title = self.cleaned_data['title']
        teacher = Teacher.objects.create(user=user, subject=subject, title=title)
        return teacher
