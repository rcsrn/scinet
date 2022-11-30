from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

def index(request):
	archivo = open('scinet_app/templates/index.html')
	plantilla = Template(archivo.read())
	archivo.close()
	contexto = Context()
	html = plantilla.render(contexto)
	return HttpResponse(html)
