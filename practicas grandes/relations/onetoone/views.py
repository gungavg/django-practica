from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant

def create(request):
    # todo crear los elementos
    place = Place(name="lugar 1", address="rio papagayo")
    place.save()
    restaurant = Restaurant(place=place, number_of_employees=24)
    restaurant.save()
    
    return HttpResponse(restaurant.place.name)