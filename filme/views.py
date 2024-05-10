from typing import Any
from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView


# Create your views here.
# def homepage(request):
#     # request pode ser GET, POST
#     return render(request, 'homepage.html')

# def homefilmes(request):
#     context = {}
#     # pegando todos os objetos do meu banco de dados
#     # uma lista com todos os filmes do meu banco de dados
#     lista_filmes = Filme.objects.all()
#     print(lista_filmes)
#     # criando uma chave no dicionario
#     context['lista_filmes'] = lista_filmes
#     return render(request, 'homefilmes.html', context)

# TemplateView A classe TemplateView no Django é usada para exibir páginas da web que não exigem nenhum processamento de dados do banco de dados, como páginas estáticas, páginas de ajuda ou páginas de contato. Em outras palavras, é usada quando você só precisa renderizar um modelo de template sem lidar diretamente com dados do banco de dados.
class Homepage(TemplateView):
    template_name = 'homepage.html'




# ListView A classe ListView no Django é usada para mostrar uma lista de itens de um modelo específico em uma página da web. Ela ajuda a buscar os itens do banco de dados e exibi-los em um formato fácil de visualizar para os usuários.
class Homefilmes(ListView):
    template_name = 'homefilmes.html' # O nome do arquivo de template que será usado para mostrar a lista de Filmes
    model = Filme
    context_object_name = 'lista_filmes'  # O nome da variável que será usada no template para acessar os itens o object_list é o padrao caso nao definimos o context


class Detalhesfilme(DetailView):
    # object é o padrao caso nao definimos o context
    template_name = 'detalhesfilme.html' # O nome do arquivo de template que será usado para mostrar os detalhes do filme
    model = Filme


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)