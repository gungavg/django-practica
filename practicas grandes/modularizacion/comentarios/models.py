from django.db import models


# Create your models here.
# este es para crear las bases de datos 
class coments(models.Model):
    # dentro del parentesis, van todos los requerimientos, es como declarar para el mysql
    name=models.CharField(max_length=255, null=False) #y este es para los char 
    score=models.IntegerField(default=3) #asi es como se declara un int 
    comment=models.TextField(max_length=1000, null=True) #este es para textos gfrandes
    date = models.DateField(null=True)
    def __str__(self):
        return self.name