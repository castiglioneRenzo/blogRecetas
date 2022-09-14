from django.urls import path
from blog.views import *
urlpatterns = [
    path('', inicio, name='inicio'),
    path('inicio', inicio, name='inicio'),
    path('login', login, name='login'),
    path('entrada/<entr_id>',mostrarEntrada, name='mostrarEntrada'),
]
