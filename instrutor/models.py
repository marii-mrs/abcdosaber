from django.db import models
from django.urls import reverse
from titulo.models import Titulo

class Instrutor(models.Model):
    """Modelo representando um Instrutor"""
    
    id = models.AutoField(primary_key=True)
    
    rg = models.CharField(max_length=20, help_text='Rg')
    
    nome = models.CharField(max_length=50, help_text='Nome')
    
    dataNascimento = models.DateField(null=True, blank=True, help_text='Data de Nascimento')
    
    telefone = models.CharField(max_length=9, help_text='Informe seu telefone:')
    
    DDD = models.CharField(max_length=3, help_text='Informe o DDD')
    
    titulo = models.ForeignKey(Titulo, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f' {self.id} - {self.nome}'