from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime, timedelta
from django.utils import timezone
#from clinica.forms import clienteForm
from django.views.generic import ListView, DetailView

from clinica.models import clientes, historial, citas

# Create your views here.
#------------------------------- Principal ------------------------------------------------------

def index(request):
	mytime = datetime.strptime('2359','%H%M').time()
	final_dia = datetime.combine(datetime.today(), mytime)
	las_citas = citas.objects.filter(fecha__gte = datetime.now(), fecha__lte = final_dia).order_by('fecha')
	context = {'las_citas': las_citas }
	return render(request, 'clinica/index.html', context)

#------------------------- Listado Pacientes -----------------------------------------------------

#def pacientes(request):
#	los_pacientes = clientes.objects.all()
#	context = {'los_pacientes': los_pacientes }
#	return render(request, 'clinica/pacientes.html', context)

class ListaPacientes(ListView):
    #model = clientes
    queryset = clientes.objects.order_by('apellidos')
    context_object_name = 'clientes'
    paginate_by = 8
#    context_object_name = 'clientes'
#    queryset = clientes.objects.filter(nombre='Javier')

#----------------------------------- Historial por cliente ---------------------------------

class ListaHistorial(ListView):

    def get_queryset(self):
        self.cliente = get_object_or_404(clientes, id=self.args[0])
        return historial.objects.filter(cliente=self.cliente).order_by('-fecha')
    def get_context_data(self,**kwargs):
        context = super(ListaHistorial,self).get_context_data(**kwargs)
        context['cliente']=self.cliente
        return context

#----------------------------------- Citas por cliente ---------------------------------

class ListaCitas(ListView):
    paginate_by = 7
    def get_queryset(self):
        self.cliente = get_object_or_404(clientes, id=self.args[0])
        return citas.objects.filter(cliente=self.cliente).order_by('-fecha')
    def get_context_data(self,**kwargs):
        context = super(ListaCitas,self).get_context_data(**kwargs)
        context['cliente']=self.cliente
        return context
#----------------------------------- Detalle Pacientes ---------------------------------
#def pacientes_detalle(request, clientes_id):
#	cliente_detalle = get_object_or_404(clientes, pk=clientes_id)
#	return render(request, 'clinica/pacientes_detalle.html', {'cliente_detalle': cliente_detalle})
class DetallePacientes(DetailView):
    model = clientes

#----------------------------- Nuevo Paciente ---------------------------------------

#def paciente_nuevo(request):
#   if request.method=='POST':
#        formulario = clienteForm(request.POST, request.FILES)
#        if formulario.is_valid():
#            formulario.save()
#            return HttpResponseRedirect('/index')
#    else:
#        formulario = clienteForm()
#    return render_to_response('clinica/clienteform.html',{'formulario':formulario}, context_instance=RequestContext(request))

#------------------------------ Borrado Pacientes  --------------------------------------

def clientesDelete(request, clientes_id):
    cliente_detalle = get_object_or_404(clientes, pk=clientes_id)
    cliente_detalle.delete()
    return HttpResponseRedirect('/pacientes')

#------------------------------ Buscar Pacientes  ---------------------------------------

def buscar_paciente(request):
	return render(request, 'clinica/paciente_buscar.html')

#------------------------------Resultado busqueda pacientes  ----------------------------
def resultado_paciente(request):
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		campo = request.GET['campo']
		filtro = campo + '__icontains'
		busqueda = clientes.objects.filter(**{filtro: q})
		return render(request, 'clinica/paciente_resultados.html', {'busqueda': busqueda, 'query':q})
	else:
		return render(request, 'clinica/paciente_buscar.html', {'error': True})

#------------------------------ Borrado Historial  --------------------------------------

def historialDelete(request, historial_id):
    historial_detalle = get_object_or_404(historial, pk=historial_id)
    historia = historial.objects.get(id = historial_id)
    numero = str(historia.cliente.id)
    historial_detalle.delete()
    return HttpResponseRedirect('/historial/' + numero + '/')

