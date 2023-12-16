from django import forms
from .models import User, Paciente, Atencion

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['rut', 'nombre', 'apellido', 'direccion']

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['rut', 'nombre', 'apellido', 'direccion','habilitado']

class AtencionForm(forms.ModelForm):
    class Meta:
        model = Atencion
        fields = ['sbp', 'dbp', 'pulso', 'temperatura', 'saturacion', 'procedimiento','practicante','razonIngreso']