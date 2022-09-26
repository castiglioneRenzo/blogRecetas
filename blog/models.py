from distutils.command.upload import upload
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils.timezone import now

class Entrada(models.Model):
    # - Titulo
    titulo = models.CharField(max_length=40)
    # - Subtitulo
    subtitulo = models.CharField(max_length=60)
    # - Autor
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    # - Fecha
    fecha = models.DateField(default=now, editable=False)
    # - Cuerpo
    cuerpo = RichTextField()
    # - Imagen
    imagen = models.ImageField(null=True, blank=True)
    # - Likes
    likes = models.ManyToManyField(User, related_name='likes')
    #__str__


    def __str__(self):
        return "Titulo: " + self.titulo + " Autor: " + str(self.autor)

    @property
    def totalLikes(self):
        return self.likes.count()