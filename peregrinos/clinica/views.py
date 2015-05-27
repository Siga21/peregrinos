from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime, timedelta
from django.utils import timezone
from clinica.forms import clienteForm
from django.views.generic import ListView, DetailView

from clinica.models import clientes, historial, citas

# Create your views here.

def index(request):
	mytime = datetime.strptime('2359','%H%M').time()
	final_dia = datetime.combine(datetime.today(), mytime)
	las_citas = citas.objects.filter(fecha__gte = datetime.now(), fecha__lte = final_dia).order_by('fecha')
	context = {'las_citas': las_citas }
	return render(request, 'clinica/index.html', context)

#--------------------------------------------------------------------

#def pacientes(request):
#	los_pacientes = clientes.objects.all()
#	context = {'los_pacientes': los_pacientes }
#	return render(request, 'clinica/pacientes.html', context)

class ListaClientes(ListView):
	model = clientes
	paginate_by = 8
	template_name = 'clinica/clientes_historial.html'

class ListaPacientes(ListView):
    model = clientes
    paginate_by = 8
#    context_object_name = 'clientes'
#    queryset = clientes.objects.filter(nombre='Javier')
#--------------------------------------------------------------------
#def pacientes_detalle(request, clientes_id):
#	cliente_detalle = get_object_or_404(clientes, pk=clientes_id)
#	return render(request, 'clinica/pacientes_detalle.html', {'cliente_detalle': cliente_detalle})
class DetallePacientes(DetailView):
    model = clientes
#--------------------------------------------------------------------
def paciente_nuevo(request):
    if request.method=='POST':
        formulario = clienteForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/index')
    else:
        formulario = clienteForm()
    return render_to_response('clinica/clienteform.html',{'formulario':formulario}, context_instance=RequestContext(request))

#--------------------------------------------------------------------
def clientesDelete(request, clientes_id):
    cliente_detalle = get_object_or_404(clientes, pk=clientes_id)
    cliente_detalle.delete()
    #mytime = datetime.strptime('2359','%H%M').time()
    #final_dia = datetime.combine(datetime.today(), mytime)
    #las_citas = citas.objects.filter(fecha__gte = datetime.now(), fecha__lte = final_dia).order_by('fecha')
    #context = {'las_citas': las_citas }
    #return render(request, 'clinica/index.html', context)
    return HttpResponseRedirect('/index')
