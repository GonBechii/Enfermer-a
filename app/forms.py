from django import forms
from .models import Practicante, Paciente, Atencion

class PracticanteForm(forms.ModelForm):
    class Meta:
        model = Practicante
        fields = ['rut', 'nombre', 'apellido', 'direccion']

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['rut', 'nombre', 'apellido', 'direccion']

class AtencionForm(forms.ModelForm):
    class Meta:
        model = Atencion
        fields = ['sbp', 'dbp', 'pulso', 'temperatura', 'saturacion']