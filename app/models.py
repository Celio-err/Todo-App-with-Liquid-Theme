from django.utils import timezone
from django.db import models

# Create your models here.
class Todo(models.Model):

    class Kategoria(models.TextChoices):
        SERVISU = 'Servisu', 'Servisu'
        PERSONAL = 'Personal', 'Personal'

    class Prioridade(models.TextChoices):
        NORMAL = 'Normal', 'Normal'
        HIGH = 'High', 'High'


    titulu = models.CharField(max_length=100)
    deskrisaun = models.TextField(blank=True, null=True)
    kategoria = models.CharField(max_length=20,choices=Kategoria.choices,default=Kategoria.PERSONAL)
    prioridade = models.CharField(max_length=20,choices=Prioridade.choices,default=Prioridade.NORMAL)                                  
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    completed_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.titulu
