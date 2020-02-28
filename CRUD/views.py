from django.shortcuts import render,HttpResponse
from.models import Persona
from.forms import formularioPersona 
from django.core.serializers import serialize
from django.core import serializers
import json

# Create your views here.
def inicio(request):
    return render(request, "inicio.html")

def cargarPersona(request):
    if request.method == 'POST':
      form=formularioPersona(request.POST)
      if form.is_valid():
        form.save()
    return HttpResponse("Ok")

def listaCompleta(parameter_list):
  data =  serializers.serialize('json',Persona.objects.all() )
  serializado=json.loads(data)
  return HttpResponse(json.dumps(list(serializado)), content_type="application/json")
    
    
def obtenerPersona(request):
  if request.method=='POST':
    persona= serializers.serialize('json',Persona.objects.filter(pk=request.POST['id'] ))
    personaSerializado=json.loads(persona)
    return HttpResponse( json.dumps(personaSerializado), content_type='application/json' )  
  else:
      return HttpResponse("Ocurrio un error en la consulta de id de Persona")



def actualizarDatosPersona(request):
    pk = request.POST.get('id')
    nombre = request.POST.get('nombre')
    apellido = request.POST.get('apellido')
    correo = request.POST.get('email')
    fechaNacimiento = request.POST.get('fechaNacimiento')
    identificador = Persona.objects.filter(pk=pk)
    identificador.update(nombre=nombre,apellido=apellido,correo=correo,fechaNacimiento=fechaNacimiento)
    return HttpResponse("Actualizado")

def eliminarPersona(request):
    pk = request.POST.get('id')
    identificador = Persona.objects.filter(pk=pk)
    identificador.delete()
    return HttpResponse("Eliminado")