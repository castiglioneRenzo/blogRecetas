from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Entrada(models.Model):
    # - Titulo
    titulo = models.CharField(max_length=40)
    # - Subtitulo
    subtitulo = models.CharField(max_length=60)
    # - Autor
    autor = models.ForeignKey(User)
    # - Fecha
    fecha = models.DateField()
    # - Cuerpo
    cuerpo = RichTextField()
    # - Imagen
    imagen = models.ImageField()
    # - Likes
    likes = models.BooleanField()
