from django.contrib import admin
from .models import Product

class ProductAdmin (admin.ModelAdmin):
    #sirve para escoger las opciones que ver en el admin
    list_display = ("name","short_description", "stock")
    
    #para poner una barra de busqueda
    search_fields= ("name", "short_description")
    #para crear un filtro 
    list_filter = ("name", "stock")
# De  esta forma podremos ver los modelos desde la pagina del administrador, esto es util para que asi podamos dar acceso a otros usuarios
admin.site.register(Product,ProductAdmin)