from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from clinica.views import ListaPacientes, DetallePacientes, ListaHistorial, ListaCitas
from clinica.forms import CrearPaciente, EditarPaciente, EditarHistorial, AgregarHistorial

urlpatterns = patterns('',
	url(r'^imagenes/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^index/', 'clinica.views.index', name = 'index'),
	url(r'^pacientes/',ListaPacientes.as_view(), name = 'ListaPacientes'),
	url(r'^pacientes_detalle/(?P<pk>[0-9]+)/$', DetallePacientes.as_view(), name = 'pacientes_detalle'),
	url(r'^pacientes_borrar/(?P<clientes_id>[0-9]+)/$', 'clinica.views.clientesDelete', name = 'pacientes_borrado'),
	url(r'^paciente/agregar/$', CrearPaciente.as_view(), name='agregarpaciente'),
	url(r'^pacientes_buscar/$', 'clinica.views.buscar_paciente', name = 'paciente_buscar'),
	url(r'^pacientes_resultado/$', 'clinica.views.resultado_paciente', name = 'paciente_resultado'),
	url(r'^historial/([\w]+)/$', ListaHistorial.as_view(), name='listahistorial' ),
	url(r'^citas/([\w]+)/$', ListaCitas.as_view(), name='listacitas' ),
	url(r'^pacientes_editar/(?P<pk>[0-9]+)/$', EditarPaciente.as_view(), name = 'pacientes_editar'),
	url(r'^historial_editar/(?P<pk>[0-9]+)/$', EditarHistorial.as_view(), name = 'historial_editar'),
	url(r'^historial_agregar/(?P<id>[0-9]+)/$', AgregarHistorial.as_view(), name = 'historial_agregar'),
    url(r'^historial_borrar/(?P<historial_id>[0-9]+)/$', 'clinica.views.historialDelete', name = 'historial_borrado'),
	url(r'^calendario/', 'clinica.views.calendario', name = 'calendario'),
)

if settings.DEBUG:
     urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
