from django.db import models
from django.urls import reverse

# Create your models here.

class TipoDeAtividade(models.Model):
    """Modelo representando um Tipo de Atividade"""
    codigo= models.AutoField(primary_key=True,
                                help_text='Código do Tipo de atividade')
    descricao= models.CharField(max_length=100, null=False,
                                help_text='Informe a descrição do Tipo de atividade')
    
    def str(self):
        return f'{self.codigo} {self.descricao}'
