from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Mensaje(models.Model):
    # - Emisor
    emisor = models.ForeignKey(User, on_delete=models.CASCADE)
    # - Remitente
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='remitente')
    # - Asunto
    asunto = models.CharField(max_length=50, default='')
    # - Cuerpo
    cuerpo = RichTextField()
    # - Leido
    leido = models.BooleanField(default=False)