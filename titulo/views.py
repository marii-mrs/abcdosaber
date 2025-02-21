from django.shortcuts import render
from django.http import HttpResponse

from tipodeatividade.models import TipoDeAtividade

# Create your views here.
def index(request):
    return HttpResponse('"<!DOCTYPE html><html><head><title>Titulo</title></head><body><h1>Titulo</h1></body></html>"')

def listar(request):
    lista_tipodeatividade = TipoDeAtividade.objects.all("descricao")
    resposta = "<u>"
    for tipodeatividade in lista_tipodeatividade:
        resposta += '<li>{0}</li>'.format(tipodeatividade)
         
        resposta += "</ul>"
        print(resposta)   
    return HttpResponse('resposta')

def show_mensagem(request):
    x = "M"
    nome = x + "arcos, tudo bem?"
    return HttpResponse(f"Bom dia!{nome}")