from django.db import models

# Create your models here.
# Se crea la clase familia

class Auto(models.Model):

    marca=models.CharField(max_length=40)
    modelo=models.CharField(max_length=40)
    anio_lanzamiento=models.IntegerField()
  