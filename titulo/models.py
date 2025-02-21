from django.db import models

# Create your models here.
class Titulo(models.Model):
    """Modelo representando um Titulo"""
    codigo = models.AutoField(primary_key=True,
                                help_text='Código do Titulo')
    descricao = models.CharField(max_length=100, null=False,
                                help_text='Informe a descrição do Titulo')
    
    def __str__(self):
        return f'{self.codigo} {self.descricao}'