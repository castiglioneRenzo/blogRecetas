from django.urls import path, include
from blog.views import *
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', inicio, name='inicio'),
    path('inicio', inicio, name='inicio'),
    path('pages', mostrarEntradas, name='pages'),
    path('login', loginRequest, name='login'),
    path('entrada/<entr_id>',mostrarEntrada, name='mostrarEntrada'),
    path('inicioUsuario', mostrarEntradasUsuario, name='inicioUsuario'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('registro', registrarUsuario, name='registrarUsuario'),
    path('editarperfil', editarPerfil, name='editarPerfil'),
    path('nuevaEntrada', nuevaEntrada, name='nuevaEntrada'),
    path('editarEntrada/<entr_id>', editarEntrada, name='editarEntrada'),
    path('eliminarEntrada/<entr_id>', eliminarEntrada, name='eliminarEntrada'),
    path('megusta/<entr_id>', likeEntrada, name='megusta'),   
    path('favoritos', entradasFavoritas, name='favoritos'),
    path('about', about, name='about') ,
]