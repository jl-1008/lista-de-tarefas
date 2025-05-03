# tasks/forms.py
from django import forms
from .models import Task
from django.contrib.auth.models import User
from datetime import datetime, date  # Adicionado 'date' à importação

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
        }
        # Define widget para o campo de data de vencimento
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})  # Exibe seletor de data no navegador
        }

    # Valida o campo de data de vencimento
    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date:
            # O widget DateInput já retorna um objeto date, então não precisa converter
            if not isinstance(due_date, date):
                raise forms.ValidationError('Digite uma data válida no formato DD/MM/AAAA.')
        return due_date

# Formulário para registro de novos usuários
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')  # Campo para senha com widget de senha

    class Meta:
        model = User  # Modelo associado: User
        fields = ['username', 'email', 'password']  # Campos exibidos no formulário
        labels = {
            'username': 'Nome de Usuário',  # Rótulo para username
            'email': 'E-mail',  # Rótulo para email
            'password': 'Senha'  # Rótulo para senha
        }

# Código antigo comentado para referência:
# username = forms.CharField(label="Nome de usuário", help_text="")  # Campo para username, sem mensagem padrão
# def save(self, commit=True):  # Sobrescreve save para criptografar a senha
#     user = super().save(commit=False)
#     user.set_password(self.cleaned_data['password'])
#     if commit:
#         user.save()
#     return user