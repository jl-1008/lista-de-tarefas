# tasks/views.py
# Importações necessárias para views, modelos, formulários e autenticação
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Task
from .forms import TaskForm, UserRegistrationForm

# View para registro de novos usuários
def register(request):
    if request.method == 'POST':  # Se o formulário foi enviado
        form = UserRegistrationForm(request.POST)  # Cria formulário com dados
        if form.is_valid():  # Verifica se é válido
            user = form.save()  # Salva usuário (senha já criptografada no forms.py)
            return redirect('login')  # Redireciona para login
    else:  # Método GET
        form = UserRegistrationForm()  # Cria formulário vazio
    return render(request, 'tasks/register.html', {'form': form})  # Renderiza template

# View para login de usuários
def user_login(request):
    if request.method == 'POST':  # Se o formulário foi enviado
        form = AuthenticationForm(request, data=request.POST)  # Cria formulário com dados
        if form.is_valid():  # Verifica se é válido
            user = form.get_user()  # Obtém usuário autenticado
            login(request, user)  # Faz login
            return redirect('task_list')  # Redireciona para lista de tarefas
    else:  # Método GET
        form = AuthenticationForm()  # Cria formulário vazio
    return render(request, 'tasks/login.html', {'form': form})  # Renderiza template

# View para logout
def user_logout(request):
    logout(request)  # Encerra sessão do usuário
    return redirect('task_list')  # Redireciona para lista de tarefas

# View para listar tarefas com filtro
@login_required  # Requer login
def task_list(request):
    filter_type = request.GET.get('filter', 'all')  # Pega parâmetro de filtro da URL
    if filter_type == 'completed':  # Filtra tarefas concluídas
        tasks = Task.objects.filter(completed=True)
    elif filter_type == 'pending':  # Filtra tarefas pendentes
        tasks = Task.objects.filter(completed=False)
    else:  # Mostra todas as tarefas
        tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'filter_type': filter_type})  # Renderiza template

# View para detalhes de uma tarefa
@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)  # Obtém tarefa pelo ID ou retorna 404
    return render(request, 'tasks/task_detail.html', {'task': task})  # Renderiza template

# View para criar nova tarefa
@login_required
def task_new(request):
    if request.method == 'POST':  # Se o formulário foi enviado
        form = TaskForm(request.POST)  # Cria formulário com dados
        if form.is_valid():  # Verifica se é válido
            form.save()  # Salva tarefa no banco
            return redirect('task_list')  # Redireciona para lista
    else:  # Método GET
        form = TaskForm()  # Cria formulário vazio
    return render(request, 'tasks/task_new.html', {'form': form})  # Renderiza template

# View para editar tarefa
@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)  # Obtém tarefa pelo ID
    if request.method == 'POST':  # Se o formulário foi enviado
        form = TaskForm(request.POST, instance=task)  # Cria formulário com dados e tarefa existente
        if form.is_valid():  # Verifica se é válido
            form.save()  # Salva alterações
            return redirect('task_list')  # Redireciona para lista
    else:  # Método GET
        form = TaskForm(instance=task)  # Cria formulário com dados da tarefa
    return render(request, 'tasks/task_edit.html', {'form': form, 'task': task})  # Renderiza template

# View para deletar tarefa
@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)  # Obtém tarefa pelo ID
    if request.method == 'POST':  # Se confirmado
        task.delete()  # Deleta tarefa
        return redirect('task_list')  # Redireciona para lista
    return render(request, 'tasks/task_delete.html', {'task': task})  # Renderiza template de confirmação

# View para marcar tarefa como concluída
@login_required
def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)  # Obtém tarefa pelo ID
    task.completed = True  # Marca como concluída
    task.save()  # Salva alteração
    return redirect('task_list')  # Redireciona para lista