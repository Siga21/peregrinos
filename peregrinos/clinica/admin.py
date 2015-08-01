from django.contrib import admin
from clinica.models import clientes, historial, citas, salas
# Register your models here.

admin.site.register(clientes)
admin.site.register(historial)
admin.site.register(citas)
admin.site.register(salas)
