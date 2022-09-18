from dataclasses import fields
import email
from tkinter import N
from django import forms
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class EntradaFormulario():
    titulo = forms.CharField(max_length=40)
    subtitulo = forms.CharField(max_length=60)
    autor = forms.EmailField()
    fecha = forms.DateField()
    cuerpo = forms.CharField(widget=CKEditorWidget())
    imagen = forms.ImageField()


class RegisterUserForm(UserCreationForm):    
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))    
    first_name = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Apellido',widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
    
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

        self.fields['username'].label = 'Nombre de Usuario'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Repetir Contraseña'


class UserEditForm(UserCreationForm):
    email=forms.EmailField(label='Modificar E-Mail')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    first_name=forms.CharField(label='Modificar Nombre')
    last_name=forms.CharField(label='Modificar Apellido')

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields}