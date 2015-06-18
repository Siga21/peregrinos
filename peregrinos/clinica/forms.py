#encoding:utf-8

from django.forms import ModelForm
from django import forms
from django.views.generic.edit import CreateView, UpdateView

from clinica.models import clientes, historial

#class clienteForm(ModelForm):
#	class Meta:
#		model = clientes
#		fields = "__all__"

class CrearPaciente(CreateView):
    model = clientes
    fields = ['nombre', 'apellidos', 'telefono', 'telefono2', 'fotografia',]

class EditarPaciente(UpdateView):
    model = clientes
    fields = ['nombre', 'apellidos', 'telefono', 'telefono2', 'fotografia',]

class EditarHistorial(UpdateView):
    model = historial
    fields = ['fecha', 'comentario', 'fotografia',]

class AgregarHistorial(CreateView):
    model = historial
    fields = ['cliente', 'fecha', 'comentario', 'fotografia',]

