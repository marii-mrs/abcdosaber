from django.test import TestCase
from django.http import HttpResponse

# Create your tests here.
def listar(request):
    return HttpResponse("Lista de Tipos de Atividade")