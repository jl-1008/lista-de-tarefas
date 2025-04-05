from django.shortcuts import render, redirect, get_object_or_404  # Adicionadas as importações necessárias
from .models import Task


def task_detail(request, pk): # Função que mostra os detalhes de uma tarefa
    task = get_object_or_404(Task, pk=pk)  # Pega a tarefa pelo id
    return render(request, 'tasks/task_detail.html', {'task': task})  # Renderiza o template com os detalhes da tarefa



# Função que lista todas as tarefas e manda para o template
def task_list(request):
    tasks = Task.objects.all()  # Pega todas as tarefas no banco de dados
    return render(request, 'tasks/task_list.html', {'tasks': tasks})  # Renderiza o template com as tarefas

def task_new(request): #criando uma nova tarefa
    if request.method == 'POST':  # Se o método for POST
        title = request.POST.get('title')  # Pega o título do formulário
        if title:
            Task.objects.create(title=title)  # Corrigido: "Task" com "T" maiúsculo
            return redirect('task_list')  # Redireciona para a lista de tarefas
    return render(request, 'tasks/task_new.html')  # Renderiza o template do formulário de nova tarefa

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)  # Pega a tarefa pelo id
    if request.method == "POST":
        title = request.POST.get('title')
        completed = request.POST.get('completed') == 'on'  # Verifica se a tarefa foi completada
        if title:
            task.title = title
            task.completed = completed
            task.save()
            return redirect('task_list')
    return render(request, 'tasks/task_edit.html', {'task': task})  # Renderiza o template de edição de tarefa

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)  # Pega a tarefa pelo id
    if request.method == "POST":
        task.delete()  # Deleta a tarefa
        return redirect('task_list')  # Redireciona para a lista de tarefas
    return render(request, 'tasks/task_delete.html', {'task': task})  # Renderiza o template de confirmação de deleção

def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)  # Pega a tarefa pelo id
    task.completed = True
    task.save()  # Marca a tarefa como concluída
    return redirect('task_list')  # Redireciona para a lista de tarefas