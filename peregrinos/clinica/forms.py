#encoding:utf-8

from django.forms import ModelForm
from  django import forms
from clinica.models import clientes

class clienteForm(ModelForm):
	class Meta:
		model = clientes
		fields = "__all__" 

