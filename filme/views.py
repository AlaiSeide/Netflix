from django.shortcuts import render
from .models import Filme

# Create your views here.

def homepage(request):
    # request pode ser GET, POST
    return render(request, 'homepage.html')


def homefilmes(request):
    context = {}
    # pegando todos os objetos do meu banco de dados
    # uma lista com todos os filmes do meu banco de dados
    lista_filmes = Filme.objects.all()
    print(lista_filmes)
    # criando uma chave no dicionario
    context['lista_filmes'] = lista_filmes
    return render(request, 'homefilmes.html', context)

