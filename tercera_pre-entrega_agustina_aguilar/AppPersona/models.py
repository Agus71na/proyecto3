from django.db import models

# Create your models here.

class Alumno(models.Model):
 
  nombre = models.CharField(max_length=40)
  apellido=models.CharField(max_length=40)
  edad=models.IntegerField()
  fecha_nac=models.DateField()
  genero=models.CharField(max_length=40)
  curso=models.CharField(max_length=5)

class Adulto1 (models.Model):
  nombre = models.CharField(max_length=40)
  apellido=models.CharField(max_length=40)
  edad=models.IntegerField()
  fecha_nac=models.DateField()
  genero=models.CharField(max_length=40)
  trabajo=models.CharField(max_length=50)

class Adulto2 (models.Model):
  nombre = models.CharField(max_length=40)
  apellido=models.CharField(max_length=40)
  edad=models.IntegerField()
  fecha_nac=models.DateField()
  genero=models.CharField(max_length=40)
  trabajo=models.CharField(max_length=50)

