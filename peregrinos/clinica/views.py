from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext

from clinica.models import clientes, historial, citas

# Create your views here.

def index(request):
	las_citas = citas.objects.all()
	context = {'las_citas': las_citas }
	return render(request, 'clinica/index.html', context)

#--------------------------------------------------------------------	
