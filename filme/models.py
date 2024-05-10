from django.db import models
from django.utils import timezone
import os

# Create your models here.


LISTA_CATEGORIAS = (
    ('ANALISES', 'Análises'),
    ('PROGRAMACAO', 'Programação'),
    ('APRESENTACAO', 'Apresentação'),
    ('OUTROS', 'Outros'),
)

# criar o filme
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    # Define um campo de imagem chamado 'thumb' que armazena imagens enviadas para o diretório 'thumb_filmes'
    thumb = models.ImageField(upload_to='thumb_filmes/')
    descricao = models.TextField(max_length=100000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    # este método __str__ personalizado define como os objetos deste modelo devem ser representados como strings, retornando o título do objeto. Isso é útil para facilitar a identificação e a visualização dos objetos em diferentes partes do seu aplicativo Django.
    def __str__(self):
        return self.titulo


    # def save(self, *args, **kwargs):
    #     self.thumb.name = os.path.join(*self.thumb.name.split(os.sep))
    #     super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        if isinstance(self.thumb.name, tuple):
            self.thumb.name = os.path.join(*self.thumb.name)
        super().save(*args, **kwargs)

# criar os episodios
class Episodio(models.Model):
    # definir a chave estrangeira sempre como primeiro

    # Define um campo de chave estrangeira chamado 'filme' no modelo atual.
    # Este campo estabelece uma relação com o modelo 'Filme'.
    # 'Filme' é o nome do modelo ao qual este campo está se referindo.
    # O 'related_name' é usado para acessar os episódios de um filme específico a partir do modelo Filme.
    # 'episodios' é o nome personalizado pelo qual podemos acessar os episódios de um filme.
    # 'on_delete=models.CASCADE' especifica que se um filme for excluído, todos os episódios associados a ele também serão excluídos.
    # Isso garante a integridade referencial no banco de dados.
    filme = models.ForeignKey('Filme', related_name='episodios', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self) -> str:
        return self.filme.titulo + " - " + self.titulo