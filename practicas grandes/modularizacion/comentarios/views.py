from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def test (request):
    return HttpResponse("funciona bi9en ")
def create(request):
    return HttpResponse("ruta para hacer pruebas")