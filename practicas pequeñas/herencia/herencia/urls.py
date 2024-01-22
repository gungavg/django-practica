
from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('herencia/', views.herencia, name='herencia'),
    path('',views.index, name='index'),
    path('otra/',views.otra,name ='otra')
]
