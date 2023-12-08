from django.db import models

# Create your models here.
    
class Practicante(models.Model):
    rut = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    correoE = models.EmailField(max_length=50)
    passW = models.CharField(max_length=50)

class Paciente(models.Model):
    rut = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)

class Atencion(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    paciente = models.ForeignKey(Paciente, max_length=50, on_delete=models.CASCADE)
    fechaInicio = models.CharField(max_length=50)
    fechaTermino = models.CharField(max_length=50)
    sbp = models.IntegerField()
    dbp = models.IntegerField()
    pulso = models.IntegerField()
    temperatura = models.IntegerField()
    saturacion = models.IntegerField()