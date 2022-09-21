from unicodedata import name
from django.urls import path
from mensajeria.views import *


urlpatterns = [
    path('nuevoMensaje', nuevoMensaje, name='nuevoMensaje'),
    path('bandejaEntrada', bandejaEntrada, name='bandejaEntrada'),
    path('eliminarMensaje/<id>', eliminarMensaje, name='eliminarMensaje'),
    path('responderMensaje/<id>', responderMensaje, name='responderMensaje'),
    path('mostrarMensaje/<id>', mostrarMensaje, name='mostrarMensaje'),
]