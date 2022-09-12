from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def nuevaEntrada(request):
    ''' agregar una nueva entrada (debe estar logueado)'''
    pass
@login_required
def eliminarEntrada(request):
    ''' eliminar entrada (debe ser el usuario que la creó) '''
    pass
@login_required
def editarEntrada(request):
    ''' editar una entrada en particular (debe ser el usuario que la creó)'''
    pass
@login_required
def mostrarEntradasUsuario(request):
    '''mostrar las entradas de un usuario logueado'''
def inicio(request):
    ''' mostrar todas las entradas en la página de inicio'''
    pass