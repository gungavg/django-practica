from django.shortcuts import render 
def herencia (request):
    return render(request, 'herencia.html',{})
def index(request):
    return render(request, 'index.html',{})
def otra (request):
    return render (request,'otra.html',{})