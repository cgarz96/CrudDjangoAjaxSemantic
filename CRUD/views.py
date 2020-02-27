from django.shortcuts import render,HttpResponse
from.models import Persona
from.forms import formularioPersona 
from django.core.serializers import serialize
from django.core import serializers
import json

# Create your views here.
def inicio(request):
    return render(request, "inicio.html")

def cargaPersona(request):
    if request.method == 'POST':
      nombre=request.POST['nombre']
      apellido=request.POST['apellido']
      fecha=request.POST['fechaNacimiento']
      correo=request.POST['correo']
      form=formularioPersona(request.POST)
      if form.is_valid():
        form.save()
        idPersona =  Persona.objects.last()
        response_data = {}
        response_data['id'] = str(idPersona)
        response_data['nombre'] = nombre
        response_data['fecha'] = fecha
        response_data['apellido'] = apellido
        response_data['correo'] = correo
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def listaCompleta(parameter_list):
  data =  serializers.serialize('json',Persona.objects.all() )
  serializado=json.loads(data)
  return HttpResponse(json.dumps(list(serializado)), content_type="application/json")
    
    
