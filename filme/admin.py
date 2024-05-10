from django.contrib import admin
from .models import Filme, Episodio

# Register your models here.
# registar o Filme que é o modelo para aparecer no admin
admin.site.register(Filme)
admin.site.register(Episodio)

