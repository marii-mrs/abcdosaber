from django.shortcuts import render 
from django.http import HttpResponse

from tipodeatividade.models import TipoDeAtividade

# Create your tests here.

def listar(request):
    lista_tipodeatividade = TipoDeAtividade.objects.all()
    contexto = {
        'tipodeatividade': lista_tipodeatividade,
    }
    
    return render (request, 'tipodeatividade/listaTipoDeAtividade.html', context=contexto)
