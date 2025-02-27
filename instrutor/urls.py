from django.urls import path
from . import views

app_name = 'instrutor'

urlpatterns = [ 
    path('lista/', views.listar, name='listar')
]