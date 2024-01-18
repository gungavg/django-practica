# aca van unicamente las vistas
from django.http import HttpResponse
def saludo(request):
    return HttpResponse("Hola amiwos del internet")