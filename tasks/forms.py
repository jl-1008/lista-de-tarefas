# tasks/forms.py
from django import forms
from .models import Task
from django.contrib.auth.models import User

# Formulário para registro de novos usuários

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")  # Campo para senha
    username = forms.CharField(label="Nome de usuário", help_text="")  # Campo para username, sem mensagem padrão

    class Meta:
        model = User  # Modelo associado: User
        fields = ['username', 'email']  # Campos exibidos no formulário

    def save(self, commit=True):  # Sobrescreve save para criptografar a senha
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
# Formulário para criar/editar tarefas
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'completed'] 
        labels = {
            'title': 'Título',  # Rótulo do campo título
            'description': 'Descrição',  # Rótulo do campo descrição
            'due_date': 'Data de Vencimento',  # Rótulo do campo data de vencimento
            'completed': 'Concluída'  # Rótulo do campo concluída
        } # Inclua outros campos do seu modelo, se houver

    