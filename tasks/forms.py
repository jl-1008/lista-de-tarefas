# tasks/forms.py
from django import forms
from .models import Task
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']  # Inclua outros campos do seu modelo, se houver

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(
        label = "Nome de Usuário",  # Texto que aparece no campo
        help_text= "",              # Remove a mensagem padrão
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password']        