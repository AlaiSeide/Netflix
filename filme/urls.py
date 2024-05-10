# url - que é o link
# view - para dizer o que vai acontecer se a tentar entrar naquele link
# template - que é o html


# AQUI DEFINIMOS AS URLS DO NOSSO SITE
from django.urls import path
from .views import Homepage, Homefilmes, Detalhesfilme

# Define os padrões de URL para o seu aplicativo Django
urlpatterns = [
    # Homepage é a minha view
    path('', Homepage.as_view()),
    path('filmes/', Homefilmes.as_view()),
    # o pk -> id que voce passou no seu url, é o primary_key do modelo da classe Detalhesfilme, o modelo da classe que é o Filme
    path('filmes/<int:pk>', Detalhesfilme.as_view()),
]
