from django.shortcuts import render
from django.http import HttpResponse

from titulo.models import Titulo
from titulo.forms import TituloForm

# Create your views here.
def index(request):
    return HttpResponse('"<!DOCTYPE html><html><head><title>Titulo</title></head><body><h1>Titulo</h1></body></html>"')

def listar(request):
    lista_titulo = Titulo.objects.all()
    contexto = {
        'titulo': lista_titulo
    }
    
def carregar_cadastro(request):
    return render (request, 'titulo/cadastrarTitulo.html')

def cadastrar(request):
    form= TituloForm(request.POST)
    if form.is_valid():
        dados_titulo = form.cleaned_data
        titulo= Titulo (
            descricao = dados_titulo['descricao']
        )
        
        titulo.save()
        
    return render(request, 'titulo/cadastrarTitulo.html')

