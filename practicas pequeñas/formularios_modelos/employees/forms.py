from django.forms import ModelForm
from .models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        # fields = ['name', 'last_name', 'email']
        fields='__all__'#? para traer todos los campos que hayamos modelado
        exclude = ('email',) #? para excluir algun campo especifico
        extra_fields=['salary'] #? esto es para crear nuevos campos 