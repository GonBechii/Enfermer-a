from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
    
# class Practicante(models.Model):
#     rut = models.CharField(primary_key=True, max_length=50)
#     nombre = models.CharField(max_length=50)
#     apellido = models.CharField(max_length=50)
#     direccion = models.CharField(max_length=50)
class Perfil(models.Model):
     id = models.CharField(primary_key=True, max_length=50)
     descripcion = models.CharField(max_length=50)

class User(AbstractUser):
    rut = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    perfil = models.ForeignKey(Perfil, max_length=50, on_delete=models.CASCADE)

class Paciente(models.Model):
    rut = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    habilitado = models.BooleanField(default=True)

class Atencion(models.Model):
    OPCIONES = (
        ('enfermedad', 'ENFERMEDAD'),
        ('accidente', 'ACCIDENTE'),
        ('estres', 'ESTRES')
        )
    id = models.CharField(primary_key=True, max_length=50)
    paciente = models.ForeignKey(Paciente, max_length=50, on_delete=models.CASCADE)
    fechaInicio = models.CharField(max_length=50)
    fechaTermino = models.CharField(max_length=50)
    sbp = models.IntegerField()
    dbp = models.IntegerField()
    pulso = models.IntegerField()
    temperatura = models.IntegerField()
    saturacion = models.IntegerField()
    procedimiento = models.TextField()
    razonIngreso = models.CharField(max_length=100, choices=OPCIONES)

    # ---------------- CAMPOS EN PROCESO DE EVALUACION ---------------------#
    # motivo_consulta = models.CharField(max_length=50, default='No motivo')
    practicante = models.ForeignKey(User, max_length=50, on_delete=models.CASCADE)
    terms = models.BooleanField(default=False)