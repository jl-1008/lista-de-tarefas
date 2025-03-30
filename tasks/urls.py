from django.urls import path
from . import views # Importa as views do app tasks

# Lista de rotas do app tasks
urlpatterns = [
    path('', views.task_list, name='task_list'), # Rota que lista as tarefas
    path('task/<int:pk>/', views.task_detail, name='task_detail'), # Rota que mostra detalhes de uma tarefa
    path('task/new/', views.task_new, name='task_new'), # Rota para criar uma nova tarefa
    path('task/<int:pk>/edit/', views.task_edit, name='task_edit'), # Rota para editar uma tarefa
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'), # Rota para deletar uma tarefa
     path('task/<int:pk>/complete/', views.task_complete, name='task_complete'), # Rota para completar uma tarefa
]