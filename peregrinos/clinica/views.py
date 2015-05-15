from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime, timedelta
from django.utils import timezone

from clinica.models import clientes, historial, citas

# Create your views here.

def index(request):
	mytime = datetime.strptime('2359','%H%M').time()
	final_dia = datetime.combine(datetime.today(), mytime)
	las_citas = citas.objects.filter(fecha__gte = datetime.now(), fecha__lte = final_dia).order_by('fecha')
	context = {'las_citas': las_citas }
	return render(request, 'clinica/index.html', context)

#--------------------------------------------------------------------	
