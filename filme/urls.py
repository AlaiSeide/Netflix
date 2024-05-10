# url - que é o link
# view - para dizer o que vai acontecer se a tentar entrar naquele link
# template - que é o html


# AQUI DEFINIMOS AS URLS DO NOSSO SITE
from django.urls import path
from .views import Homepage, Homefilmes, Detalhesfilme

app_name = 'filme'

# Define os padrões de URL para o seu aplicativo Django
urlpatterns = [
    # Homepage é a minha view
    path('', Homepage.as_view(), name='homepage'),
    # Claro! O name='homefilmes' dentro da sua URL em Django é como um apelido que você dá para essa rota. É como dar um nome único a um endereço na internet. Então, quando você precisar usar esse endereço em outras partes do seu código, em vez de escrever a URL completa, você só precisa usar esse apelido.Por exemplo, se você quiser criar um link para essa página em um arquivo HTML, em vez de escrever toda a URL, você simplesmente usa o apelido:
    # ex: <a href="{% url 'homefilmes' %}">Página Inicial de Filmes</a>
    path('filmes/', Homefilmes.as_view(), name='homefilmes'),
    # o pk -> id que voce passou no seu url, é o primary_key do modelo da classe Detalhesfilme, o modelo da classe que é o Filme
    path('filmes/<int:pk>', Detalhesfilme.as_view(), name='detalhesfilme'),
]
