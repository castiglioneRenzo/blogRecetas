from django.urls import path
from blog.views import *
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', inicio, name='inicio'),
    path('inicio', inicio, name='inicio'),
    path('login', loginRequest, name='login'),
    path('entrada/<entr_id>',mostrarEntrada, name='mostrarEntrada'),
    path('inicioUsuario', mostrarEntradasUsuario, name='inicioUsuario'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('registro', registrarUsuario, name='registrarUsuario'),
    path('editarperfil', editarPerfil, name='editarPerfil'),
]
