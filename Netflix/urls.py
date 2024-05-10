"""
URL configuration for Netflix project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# AQUI DEFINIMOS AS URLS DO NOSSO SITE
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# Define os padrões de URL para o seu aplicativo Django
urlpatterns = [
    # Define a URL para a interface de administração do Django
    path('admin/', admin.site.urls),
    # include('filme.urls'): Isso inclui as rotas definidas no arquivo urls.py do aplicativo filme. O Django procurará neste arquivo por padrões de URL adicionais sempre que o URL raiz for solicitado.

    # O namespace='filme' é como um sobrenome para as URLs da sua aplicação de filmes. Ele ajuda a diferenciar e organizar as URLs de diferentes partes do seu projeto.
    # Por exemplo, imagine que você tem um site que inclui seções para filmes, séries e músicas. Cada seção tem sua própria página inicial. Com o namespace, você pode dar um nome único para as URLs de cada seção.
    # ex: <a href="{% url 'filme:home' %}">Página Inicial de Filmes</a>, Aqui, 'filme:home' diz ao Django para procurar a URL chamada "home" dentro do namespace "filme".
    path('', include('filme.urls', namespace='filme')),
]

# Adiciona a URL de arquivos estáticos ao urlpatterns
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Adiciona a URL de arquivos de mídia ao urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)