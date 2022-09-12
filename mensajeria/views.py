from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def nuevoMensaje(request):
    ''' se crea y envía un nuevo mensaje (usuario debe estar logueado) '''
    pass
@login_required
def eliminarMensaje(request):
    ''' se elimina un mensaje de la bandeja de mensajes de un usuario logueado '''
    pass
@login_required
def mostrarMensaje(request):
    ''' se muestra un mensaje y se marca como leído '''
    pass
@login_required
def responderMensaje(request):
    ''' se responde a un mensaje en la bandeja de mensajes de un usuario logueado '''
    pass