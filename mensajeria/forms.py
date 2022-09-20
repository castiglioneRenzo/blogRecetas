from tkinter import N
from tkinter.tix import Tree
from django.forms import ModelForm, ModelChoiceField
from ckeditor.widgets import CKEditorWidget
from mensajeria.models import Mensaje
from django.contrib.auth.models import User
from django import forms


class MensajeForm(ModelForm):
    class Meta:
        model = Mensaje
        fields = ['remitente', 'asunto', 'cuerpo']
    def __init__(self, *args, **kwargs):
        super(MensajeForm, self).__init__(*args, **kwargs)
        # self.fields['remitente']=ModelChoiceField(queryset=User.objects.all())
        self.fields['remitente'].label='Para:'