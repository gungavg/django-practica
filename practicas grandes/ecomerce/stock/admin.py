from django.contrib import admin
from .models import Product
# De  esta forma podremos ver los modelos desde la pagina del administrador, esto es util para que asi podamos dar acceso a otros usuarios
admin.site.register(Product)