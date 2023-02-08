from django.db import forms


class AlumnoFormulario(forms.Form):
 
  nombre = forms.CharField(max_length=40)
  apellido=forms.CharField(max_length=40)
  edad=forms.IntegerField()
  fecha_nac=forms.DateField()
  genero=forms.CharField(max_length=40)
  curso=forms.CharField(max_length=5)

class Adulto1Formulario (forms.Form):
  nombre = forms.CharField(max_length=40)
  apellido=forms.CharField(max_length=40)
  edad=forms.IntegerField()
  fecha_nac=forms.DateField()
  genero=forms.CharField(max_length=40)
  trabajo=forms.CharField(max_length=50)

class Adulto2Formulario (forms.Form):
  nombre = forms.CharField(max_length=40)
  apellido=forms.CharField(max_length=40)
  edad=forms.IntegerField()
  fecha_nac=forms.DateField()
  genero=forms.CharField(max_length=40)
  trabajo=forms.CharField(max_length=50)

