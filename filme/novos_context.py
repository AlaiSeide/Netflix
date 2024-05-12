# criando uma variavel que todas as nossas paginas html vao ter

from .models import Filme

def lista_filmes_recentes(request):
    # Definindo a função lista_filmes_recentes que recebe um objeto request como parâmetro
    # Buscando todos os filmes no banco de dados, ordenando-os em ordem decrescente de data de criação e pegando os 10 primeiros
    # 'data_criacao' é o nome do campo da sua tabela de filmes que representa a data de criação
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:10]

    # Retornando um dicionário com a chave 'lista_filmes_recentes' e a lista de filmes como valor
    return {'lista_filmes_recentes': lista_filmes}



def lista_filmes_emalta(request): # Definindo a função lista_filmes_emalta que recebe um objeto request como parâmetro
    # Buscando todos os filmes no banco de dados, ordenando-os em ordem decrescente de visualizações e pegando os 10 primeiros
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:10] 

     # Retornando um dicionário com a chave 'lista_filmes_emalta' e a lista de filmes como valor
    return {'lista_filmes_emalta': lista_filmes} 