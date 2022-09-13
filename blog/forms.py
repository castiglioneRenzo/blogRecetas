from django import forms
from ckeditor.widgets import CKEditorWidget
class EntradaFormulario():
    titulo = forms.CharField(max_length=40)
    subtitulo = forms.CharField(max_length=60)
    autor = forms.EmailField()
    fecha = forms.DateField()
    cuerpo = forms.CharField(widget=CKEditorWidget())
    imagen = forms.ImageField()