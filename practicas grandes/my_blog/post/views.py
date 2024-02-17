from django.shortcuts import render

from .models import Author, Entry
# Create your views here.
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
    
    return render (request, 'post/queries.html', {'authors':authors,'filtered':filltered,'author':author,'limit':limit, 'offsets': offsets})