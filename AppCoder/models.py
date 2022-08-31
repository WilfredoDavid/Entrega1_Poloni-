from django.db import models

# Create your models here.
# Se crea la clase familia

class Paises(models.Model):
    nombre=models.CharField(max_length=20)
    continente=models.CharField(max_length=20)
    empresas_automotrices=models.CharField(max_length=50)
      
class Empresas(models.Model):
    nombre=models.CharField(max_length=30)
    fecha_creacion=models.DateField()
    area=models.CharField(max_length=30)

class Autos(models.Model):
    modelo=models.CharField(max_length=20)
    fecha_lanzamiento=models.DateField()
    velocidad_maxima=models.IntegerField()
    transmision_automatica=models.CharField(max_length=10)
    transmision_manual=models.CharField(max_length=10)
  