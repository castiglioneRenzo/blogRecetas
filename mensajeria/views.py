from contextlib import redirect_stderr
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from mensajeria.forms import MensajeForm
from django.contrib import messages
from mensajeria.models import Mensaje
from django.db.models import Q


@login_required
def nuevoMensaje(request):
    ''' se crea y envía un nuevo mensaje (usuario debe estar logueado) '''        
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if(form.is_valid()):
            msg = form.save(commit=False)
            msg.emisor=request.user
            msg.save()
            messages.success(request, "Se envió el mensaje")
            return redirect('mensajeria:bandejaEntrada')
        else:
            messages.error(request, "El mensaje no se pudo enviar correctamente")
            return redirect('mensajeria:bandejaEntrada')
    else:        
        form = MensajeForm()
        return render(request, 'mensajeria/nuevoMensaje.html', {"form":form})


@login_required
def eliminarMensaje(request, id):
    ''' se elimina un mensaje de la bandeja de mensajes de un usuario logueado '''
    mensaje = Mensaje.objects.get(id=id)
    mensaje.delete()
    messages.success(request, "Se elimino el mensaje")
    return redirect('mensajeria:bandejaEntrada')


@login_required
def mostrarMensaje(request, id):
    ''' se muestra un mensaje y se marca como leído '''
    mensaje = Mensaje.objects.get(id=id)
    # mensaje.visto=True
    # mensaje.save()
    return render(request, 'mensajeria/mostrarMensaje.html', {'mensaje':mensaje})


@login_required
def responderMensaje(request):
    ''' se responde a un mensaje en la bandeja de mensajes de un usuario logueado '''
    pass


@login_required
def bandejaEntrada(request):
    ''' se muestra la bandeja de entrada del usuario logueado '''
    mensajes = Mensaje.objects.filter(Q(emisor=request.user) | Q(remitente=request.user))
    return render(request, 'mensajeria/bandejaEntrada.html', {"mensajes":mensajes})