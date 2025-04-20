from django.db import models

class Task(models.Model):
    
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200) # Campo pra título da tarefa, até 200 caracteres
    description = models.TextField(blank=True)  # Descrição opcional
    due_date = models.DateField(null=True, blank=True)  # Data de vencimento opcional
    completed = models.BooleanField(default=False)  # Indica se a tarefa tá concluída, padrão é falso
    created = models.DateTimeField(auto_now_add=True) # Data de criação da tarefa, preenchida automaticamente

    def __str__(self):
        # Mostra o título no admin e shell
        return self.title

