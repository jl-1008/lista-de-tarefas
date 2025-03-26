from django.shortcuts import render
from .models import Task
# Importa o medelo Task para pegar os dados


# Função que lista todas as tarefas e manda para o template
def task_list(request):
    tasks = Task.object.all() #Busca todas as tarefas no banco de dados
    return render(request, 'tasks/task_list.html' , {'tasks': tasks}) # Renderiza o template com as tarefas