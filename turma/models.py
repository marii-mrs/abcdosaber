from django.db import models
from django.urls import reverse

from tipodeatividade.models import TipoDeAtividade
from aluno.models import Aluno
from instrutor.models import Instrutor

from django.db import models
from django.utils import timezone

from tipodeatividade.models import TipoDeAtividade
from instrutor.models import Instrutor
from aluno.models import Aluno


# Create your models here.
class Turma(models.Model):
    numero = models.AutoField(primary_key=True, help_text="Informe a turma do Aluno")
    horario_aula = models.TimeField(
        help_text="Informe a hora em que a hora da aula da Turma"
    )
    duracao_aula = models.SmallIntegerField(
        default=30, help_text="Informe a duração da aula da Turma"
        )
    data_inicial = models.DateField(
        default=timezone.now(), help_text="Informe a data inicial da Turma"
    )
    data_final = models.DateField(
        default=timezone.now(), help_text="Informe a data final da Turma"
    )
    codigo_atividade = models.ForeignKey(TipoDeAtividade, on_delete=models.CASCADE)
    matricula_monitor = models.ForeignKey(
        Aluno, null=True, blank=True, on_delete=models.SET_NULL
    )
    id_instrutor = models.ForeignKey(Instrutor, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ["numero"]

    def __str__(self):
        return (
            f"{self.numero} - {self.id_instrutor.nome} - {self.matricula_monitor.nome}"
        )


class TurmaAluno(models.Model):
    turma_numero = models.ForeignKey(
        Turma, on_delete=models.CASCADE, help_text="Número da Turma"
    )

    matricula_aluno = models.ForeignKey(
        Aluno, on_delete=models.CASCADE, help_text="Matrícula do Aluno"
    )

    data_inicio_matricula = models.DateField(
        null=False, default=timezone.now, help_text="Numero Matrícula do aluno"
    )

    data_fim_matricula = models.DateField(
        null=True, blank=True, help_text="Data Fim Matrícula do aluno"
    )

    def __str__(self):
        reposta = f'{self.turma_numero} - {self.matricula_aluno} - {self.data_inicio_matricula.strftime("%d/%m/%Y")}'
        data_fim_matricula = (
            self.data_fim_matricula.strftime("%d/%m/%Y")
            if self.data_fim_matricula
            else ""
        )

        if data_fim_matricula:
            resposta += f" - {data_fim_matricula}"

        return reposta


class Ausencia(models.Model):
    turma_numero = models.ForeignKey(
        Turma, on_delete=models.CASCADE, help_text="Número da Turma"
    )

    matricula_aluno = models.ForeignKey(
        Aluno, on_delete=models.CASCADE, help_text="Matrícula do Aluno"
    )

    data_ausencia = models.DateField(
        null=False, default=timezone.now, help_text="Data falta do aluno"
    )
    
    
    def str(self):
        resposta = f' Turma:{self.numero_turma} - Aluno:{self.matricula_aluno} '
              
        return resposta
    
    