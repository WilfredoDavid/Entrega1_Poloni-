from django.db import models

# Create your models here.
# Se crea la clase familia

class Familiar(models.Model):

    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    parentesco=models.CharField(max_length=40)
    fecha_de_nacimiento=models.DateTimeField(null=True, blank=True)
    edad=models.IntegerField(null=True, blank=True) 
    nota=models.CharField(max_length=40)
