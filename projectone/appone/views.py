import json
 

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import appone

#def json(request):
	#appone_table = appone.objects.all()
	#template = loader.get_template('appone/index.html')
	#context = {
	#'appone_table' : appone_table,
	#}
	#return HttpResponse(template.render(context, request))
	

def raw(request):
	#json doc to /appone/ url
	data = open('/home/pi/python/projectone/appone/refGeneData.json').read()
	#return HttpResponse(json.dumps(data), content_type='application/json')
	data_json = json.loads(data)	
	return render(request, 'appone/json_parse.html', {'o': data_json} )

def index(request):
    return render(request, 'appone/index.html')
