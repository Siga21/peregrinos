from django.db import models
from datetime import datetime

# Create your models here.

class clientes(models.Model):
    nombre = models.CharField(max_length=75)
    apellidos = models.CharField(max_length=75)
    telefono =  models.PositiveIntegerField(null=True, blank=True)
    telefono2 = models.PositiveIntegerField(null=True, blank=True)
    antiguedad = models.DateTimeField(default=datetime.now, blank=True)
    fotografia = models.ImageField(upload_to='imagenes', blank=True)

    def __unicode__(self):
    	return self.nombre


class historial(models.Model):
    cliente = models.ForeignKey(clientes, default=None, null=True, blank=True)
    fecha = models.DateTimeField(default=datetime.now, blank=True)
    comentario = models.TextField()
    fotografia = models.ImageField(upload_to='imagenes')

    def __unicode__(self):
    	return self.cliente


class citas(models.Model):
    fecha = models.DateTimeField(default=datetime.now, blank=True)
    cliente = models.ForeignKey(clientes, default=None, null=True, blank=True)
    observaciones = models.TextField()
