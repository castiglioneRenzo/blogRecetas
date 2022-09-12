from pyexpat import model
from django.db import models
from ckeditor.fields import RichTextField

class Mensaje(models.Model):
    # - Emisor
    emisor = models.EmailField()
    # - Remitente
    remitente = models.EmailField()
    # - Cuerpo
    cuerpo = RichTextField()
    # - Leido
    leido = models.BooleanField()