from django.shortcuts import render
from django.http import HttpResponse

from titulo.models import Titulo

# Create your views here.
def index(request):
    return HttpResponse('"<!DOCTYPE html><html><head><title>Titulo</title></head><body><h1>Titulo</h1></body></html>"')

def listar(request):
    lista_titulo = Titulo.objects.all()
    contexto = {
        'titulo': lista_titulo
    }
    

    resposta = "<u>"
    for titulo in titulo:
        resposta += '<li>{0}</li>'.format(titulo)
         
        resposta += "</ul>"
        print(resposta)   
    return HttpResponse('resposta')