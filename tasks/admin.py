from django.contrib import admin
from .models import Task    

# Registra o modelo Task no painel admin
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'created')  # Mostra título, status e data na lista



