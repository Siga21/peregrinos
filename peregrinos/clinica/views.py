from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from django.utils import timezone

from clinica.models import clientes, historial, citas

# Create your views here.

def index(request):
	las_citas = citas.objects.filter(fecha__gte = timezone.now()).order_by('fecha')
	context = {'las_citas': las_citas }
	return render(request, 'clinica/index.html', context)

#--------------------------------------------------------------------	
