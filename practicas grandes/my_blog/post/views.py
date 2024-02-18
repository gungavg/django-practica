from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Entry

def update(request):
    author =Author.objects.get(id=1)
    author.name="jose perez"
    author.email="joseperez@gmail.com"
    author.save()
    return HttpResponse("Se modifico correctamente")

def queries(request):
    # obtener todos los elementos que se tienen en un objeto
    authors=Author.objects.all()
    
    # obtener datos filtrados por condicion 
    filltered = Author.objects.filter(id=28)
    
    # obtener un unico objeto
    author = Author.objects.get(id=1)
    
    #* obtener  los 10 primeros  elementos que se tienen en un objeto
    limit=Author.objects.all()[:10]
    
    # obtener los 10 valores saltando los 5 primeros
    offsets = Author.objects.all()[5:10]
    
    #! metodos de ordenacion lo que en sql es order by 
    #? obtener todos los elementos que se tienen en un objeto ordenado 
    orders=Author.objects.all().order_by('email')
    
    #? obtener todos los elementos cuyo id sea menor o igual a 15
    filtered2=Author.objects.filter(id__lte=15)
    
    #? para filtrar por alguna palabra clave
    filtered3= Author.objects.filter(name__contains="sim")
    
    return render (request, 'post/queries.html', {'authors':authors,'filtered':filltered,'author':author,'limit':limit, 'offsets': offsets,'orders':orders,'filtered2':filtered2,'filtered3':filtered3})