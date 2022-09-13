from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blog.models import *
from blog.forms import *


@login_required
def nuevaEntrada(request):
    ''' agregar una nueva entrada (debe estar logueado)'''
    if request.method == 'POST':
        entradaForm = EntradaFormulario(request.POST)
        if(entradaForm.is_valid()):
            info = entradaForm.cleaned_data
            entrada = Entrada(titulo=info['titulo'], subtitulo=info['subitutlo'],autor=request.user, fecha=info['fecha'],cuerpo=info['cuerpo'], imagen=info['imagen'], likes=0)
            entrada.save()
            return render(request, 'inicio.html')
        else:
            return render(request, 'nuevaEntrada.html', {"error":"Los datos ingresados no son válidos"})
    else:
        entradaForm = EntradaFormulario()
    return render(request, 'nuevaEntrada.html', {"formulario": entradaForm})


@login_required
def eliminarEntrada(request, entr_id):
    ''' eliminar entrada (debe ser el usuario que la creó) '''
    entrada = Entrada.objects.get(id=entr_id)
    titulo = entrada.titulo
    entrada.delete()
    entradas = Entrada.objects.filter(autor=request.user)
    return render(request, 'entradasDeUsuario.html', {"entradas":entradas,"mensaje":f"Entrada {titulo} eliminada"})


@login_required
def editarEntrada(request, entr_id):
    ''' editar una entrada en particular (debe ser el usuario que la creó)'''
    entrada = Entrada.objects.get(id=entr_id)
    if request.method == 'POST':
        entradaForm = EntradaFormulario(request.POST)
        if(entradaForm.is_valid()):
            info = entradaForm.cleaned_data
            entrada.titulo = info['titulo']
            entrada.subtitulo = info['subtitulo']
            entrada.fecha = info['fecha']
            entrada.cuerpo = info['cuerpo']
            entrada.imagen = info['imagen']
            entrada.save()
            return render(request, 'inicio.html')
        else:
            return render(request, 'nuevaEntrada.html', {"error":"Los datos ingresados no son válidos"})
    else:
        entradaForm = EntradaFormulario(initial={"titulo":entrada.titulo, "subtitulo":entrada.subtitulo,"fecha":entrada.fecha,"cuerpo":entrada.cuerpo,"imagen":entrada.imagen})
    return render(request, 'nuevaEntrada.html', {"formulario": entradaForm, "entr_titulo":entr_id})


@login_required
def mostrarEntradasUsuario(request):
    '''mostrar las entradas de un usuario logueado'''
    entradas = Entrada.objects.filter(autor=request.user)
    return render(request, 'entradasDeUsuario.html', {"entradas":entradas})


def mostrarEntrada(request, entr_id):
    entrada = Entrada.objects.get(id=entr_id)
    return render(request, 'mostrarEntrada.html', {"entrada":entrada})


def likeEntrada(request, entr_id):
    entrada=Entrada.objects.get(id=entr_id)
    entrada.likes = entrada.likes + 1
    entrada.save()
    return render(request, 'mostrarEntrada.html', {"entrada":entrada, "mensaje":f"Le diste like a la publicacion {entrada.titulo}"})


def inicio(request):
    ''' mostrar todas las entradas en la página de inicio'''
    entradas = Entrada.objects.all()
    return render(request, 'inicio.html', {"entradas":entradas})