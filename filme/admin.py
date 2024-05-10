from django.contrib import admin
from .models import Filme

# Register your models here.
# registar o Filme que é o modelo para aparecer no admin
admin.site.register(Filme)
