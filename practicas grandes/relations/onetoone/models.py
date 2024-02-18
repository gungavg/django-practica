from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Restaurant(models.Model):
    # esto es para realizar la relacion con la otra clase
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)
    number_of_employees= models.IntegerField(default=1)    
    
    def __str__(self):
        return self.place.name
    