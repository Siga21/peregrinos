from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse

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

    def get_absolute_url(self):
        return reverse('pacientes_detalle', kwargs={'pk': self.pk})


class historial(models.Model):
    cliente = models.ForeignKey(clientes, default=None, null=True, blank=True)
    fecha = models.DateTimeField(default=datetime.now, blank=True)
    comentario = models.TextField()
    fotografia = models.ImageField(upload_to='imagenes', blank=True)

    def get_absolute_url(self):
        return reverse('listahistorial', args=[str(self.cliente.id)])

class salas(models.Model):
    sala = models.CharField(max_length=25)
    color = models.CharField(max_length=7)
    observaciones = models.TextField(default=None, null=True)

    def __unicode__(self):
        return self.sala

class citas(models.Model):
    fecha = models.DateTimeField(default=datetime.now, blank=True)
    cliente = models.ForeignKey(clientes, default=None, null=True, blank=True)
    observaciones = models.TextField()
    sala = models.ForeignKey(salas, default=None, null=True, blank=True)
