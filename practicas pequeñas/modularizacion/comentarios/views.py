from django.shortcuts import render
from django.http import HttpResponse 
from .models import Coment
# Create your views here.
def test (request):
    return HttpResponse("funciona bi9en ")
def create(request):
    #para crear un modelo
    #coment = Coment(name="jose",score=7,comment="este es un comentstriooo")
    #coment.save()
    #!otra forma de crear un oobjeto 
    coment = Coment.objects.create(name="pedrito")
    return HttpResponse("ruta para hacer pruebas")
def delete (request):
    #para borrar un objeto que esta dentro de nuestro modelo, se debe de buscar el objeto
    #coment = Coment.objects.get(id=1)
    #coment.delete()
    Coment.objects.filter(id=2).delete()
    
    return HttpResponse("se elimino el id")