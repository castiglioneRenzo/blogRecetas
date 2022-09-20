from functools import reduce
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blog.models import *
from blog.forms import *
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

def loginRequest(request):
    if request.method == "POST":      
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:       
            login(request, user)
            return redirect('blog:inicioUsuario')
        else:
            messages.success(request, "Usuario o contraseña invalidos...")
            return redirect('blog:login')
    else:
        return render(request, 'sign-in/index.html')

def registrarUsuario(request):
    if request.method == "POST":      
        form = RegisterUserForm(request.POST)
        if (form.is_valid()):            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('blog:inicioUsuario')
        else:
            messages.success(request, "Los datos ingresados No son validos...")
            return redirect('blog:registrarUsuario')
    else:
        form = RegisterUserForm()
        return render(request, 'registro/registrarUsuario.html', {"form":form})


@login_required        
def editarPerfil(request):
    usuario=request.user
    if (request.method=="POST"):
        form= UserEditForm(request.POST)
        if (form.is_valid()):
            usuario.first_name=form.cleaned_data["first_name"]
            usuario.last_name=form.cleaned_data["last_name"]
            usuario.email=form.cleaned_data["email"]
            usuario.password1=form.cleaned_data["password1"]
            usuario.password2=form.cleaned_data["password2"]
            usuario.save()
            return render(request, 'registro/editarPerfil.html', {'mensaje':f"Perfil de {usuario} editado"})
        else:
            messages.success(request,"Los datos no son correctos")
            return render(request, 'registro/editarPerfil.html')
    else:
        form= UserEditForm(instance=usuario)
    return render(request, 'registro/editarPerfil.html', {'form':form, 'usuario':usuario})


@login_required
def nuevaEntrada(request):
    ''' agregar una nueva entrada (debe estar logueado)'''
    if request.method == 'POST':
        entradaForm = EntradaFormulario(request.POST, request.FILES)
        if(entradaForm.is_valid()):
            info = entradaForm.cleaned_data
            entrada = Entrada(titulo=info['titulo'], subtitulo=info['subtitulo'],autor=request.user, cuerpo=info['cuerpo'], imagen=info['imagen'])
            entrada.save()
            return redirect('blog:inicioUsuario')
        else:
            print(entradaForm.errors)
            messages.error(request,"Los datos ingresados no son válidos")
            return render(request, 'album/nuevaEntrada.html')
    else:
        entradaForm = EntradaFormulario()
        return render(request, 'album/nuevaEntrada.html', {"form": entradaForm})


@login_required
def eliminarEntrada(request, entr_id):
    ''' eliminar entrada (debe ser el usuario que la creó) '''
    entrada = Entrada.objects.get(id=entr_id)
    titulo = entrada.titulo
    entrada.delete()
    print(entr_id)    
    print(entrada)
    messages.success(request, f"Entrada '{titulo}' eliminada")
    return redirect('blog:inicioUsuario')


@login_required
def editarEntrada(request, entr_id):
    ''' editar una entrada en particular (debe ser el usuario que la creó)'''
    entrada = Entrada.objects.get(id=entr_id)
    if request.method == 'POST':
        entradaForm = EntradaFormulario(request.POST, request.FILES)
        if(entradaForm.is_valid()):
            info = entradaForm.cleaned_data
            entrada.titulo = info['titulo']
            entrada.subtitulo = info['subtitulo']            
            entrada.cuerpo = info['cuerpo']
            entrada.imagen = info['imagen']
            entrada.save()
            return redirect('blog:inicioUsuario')
        else:
            print(entradaForm.errors)
            messages.success(request,"Los datos no son correctos")
            return render(request, 'album/editarEntrada.html')
    else:
        entradaForm = EntradaFormulario(initial={"titulo":entrada.titulo, "subtitulo":entrada.subtitulo,"fecha":entrada.fecha,"cuerpo":entrada.cuerpo,"imagen":entrada.imagen})
    return render(request, 'album/editarEntrada.html', {"form": entradaForm, "entr_id":entr_id})


@login_required
def mostrarEntradasUsuario(request):
    '''mostrar las entradas de un usuario logueado'''
    entradas = Entrada.objects.filter(autor=request.user)
    return render(request, 'album/entradasDeUsuario.html', {"entradas":entradas})


def mostrarEntrada(request, entr_id):
    entrada = Entrada.objects.get(id=entr_id)
    return render(request, 'album/mostrarEntrada.html', {"entrada":entrada})

@login_required(login_url='login')
def likeEntrada(request, entr_id):
    entrada=Entrada.objects.get(id=entr_id)
    entrada.likes = entrada.likes + 1
    entrada.save()
    return render(request, 'album/mostrarEntrada.html', {"entrada":entrada})


def inicio(request):
    ''' mostrar todas las entradas en la página de inicio'''
    entradas = Entrada.objects.all()
    return render(request, 'album/inicioPublico.html', {"entradas":entradas})