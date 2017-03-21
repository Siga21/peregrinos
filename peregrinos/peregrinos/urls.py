from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib import admin
from django.conf import settings
from clinica import views
from clinica.views import index, ListaPacientes, DetallePacientes, ListaHistorial, ListaCitas, ListaSalas, DetalleSalas
from clinica.forms import CrearPaciente, EditarPaciente, EditarHistorial, AgregarHistorial
from clinica.forms import CrearSala, EditarSala, EditarCita
urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^index/', views.index , name = 'index'),
	url(r'^pacientes/',ListaPacientes.as_view(), name = 'ListaPacientes'),
	url(r'^pacientes_detalle/(?P<pk>[0-9]+)/$', DetallePacientes.as_view(), name = 'pacientes_detalle'),
	url(r'^pacientes_borrar/(?P<clientes_id>[0-9]+)/$', views.clientesDelete, name = 'pacientes_borrado'),
	url(r'^paciente/agregar/$', CrearPaciente.as_view(), name='agregarpaciente'),
	url(r'^pacientes_buscar/$', views.buscar_paciente, name = 'paciente_buscar'),
	url(r'^pacientes_resultado/$', views.resultado_paciente, name = 'paciente_resultado'),
	url(r'^historial/([\w]+)/$', ListaHistorial.as_view(), name='listahistorial' ),
	url(r'^citas/([\w]+)/$', ListaCitas.as_view(), name='listacitas' ),
	url(r'^pacientes_editar/(?P<pk>[0-9]+)/$', EditarPaciente.as_view(), name = 'pacientes_editar'),
	url(r'^historial_editar/(?P<pk>[0-9]+)/$', EditarHistorial.as_view(), name = 'historial_editar'),
	url(r'^historial_agregar/(?P<id>[0-9]+)/$', AgregarHistorial.as_view(), name = 'historial_agregar'),
    url(r'^historial_borrar/(?P<historial_id>[0-9]+)/$', views.historialDelete, name = 'historial_borrado'),
	url(r'^calendario/', views.calendario, name = 'calendario'),
	url(r'^salas/',ListaSalas.as_view(), name = 'ListaSalas'),
	url(r'^salas_detalle/(?P<pk>[0-9]+)/$', DetalleSalas.as_view(), name = 'salas_detalle'),
	url(r'^sala/agregar/$', CrearSala.as_view(), name='agregarsala'),
	url(r'^sala/editar/(?P<pk>[0-9]+)/$', EditarSala.as_view(), name = 'sala_editar'),
	url(r'^sala/borrar/(?P<salas_id>[0-9]+)/$', views.salasDelete, name = 'salas_borrado'),
	url(r'^citas_modificar/(?P<pk>[0-9]+)/$', EditarCita.as_view(), name = 'citas_editar'),
]

if settings.DEBUG:
     urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
