from django.db import models

class Task(models.Model):
    # Campo pra título da tarefa, até 200 caracteres
    title = models.CharField(max_length=200)
    # Indica se a tarefa tá concluída, padrão é falso
    complete = models.BooleanField(default=False)
    # Data de criação da tarefa, preenchida automaticamente
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Mostra o título no admin e shell
        return self.title

