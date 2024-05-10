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
    path('', include('filme.urls')),
]

# Adiciona a URL de arquivos estáticos ao urlpatterns
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Adiciona a URL de arquivos de mídia ao urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)