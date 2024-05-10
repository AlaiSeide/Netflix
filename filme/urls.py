# url - que é o link
# view - para dizer o que vai acontecer se a tentar entrar naquele link
# template - que é o html


# AQUI DEFINIMOS AS URLS DO NOSSO SITE
from django.urls import path
from .views import homepage, homefilmes

# Define os padrões de URL para o seu aplicativo Django
urlpatterns = [
    # homepage é a minha view
    path('', homepage),
    path('filmes/', homefilmes),

]
