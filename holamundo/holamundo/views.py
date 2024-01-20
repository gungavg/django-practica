# aca van unicamente las vistas
from django.http import HttpResponse
def saludo(request):
    return HttpResponse("Hola amiwos del internet")


#rutas con parametros
def adulto(request,edad):
    if edad >=18:
        return HttpResponse("eres mayor de edad")
    else:
        return HttpResponse("no eres mayor de edad")