"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from tasks.views import user_login, register, user_logout  # Importa as views personalizadas

# Rotas principais do projeto
urlpatterns = [
    path('', user_login, name='home'), # Rota raiz vai para o login
    path('admin/', admin.site.urls), # Rota para o admin
    path('tasks/', include('tasks.urls')),  # Inclui as rotas do app tasks
    path('login/', user_login, name='login'), # Rota para login
    path('logout/', user_logout, name='logout'), # Rota para logout
    path('register/', register, name='register'), # Rota para registro
]
