from django.shortcuts import render
from AppPersona.models import *
from AppPersona.forms import *
# Create your views here.

def ver_alumno(request):
 
 todas = Alumno.objects.all

 return render(request,"AppPersona/verAlumno.html",{"todas":todas})
 
def ver_adulto1(request):
 
 
 return render(request,"AppPersona/verAdulto1.html")

def ver_adulto2(request):
 
 
 return render(request,"AppPersona/verAdulto2.html")

def agregar_alumno (request):
 
      if request.method == "POST":
 
            miFormulario = AlumnoFormulario (request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  Alumno = Alumno(nombre=informacion["nombre"],apellido=informacion["apellido"], edad=informacion["edad"], fecha_nac=informacion["fecha"],genero=informacion["genero"],curso=informacion["curso"],)
                  Alumno.save()
                  return render(request, "AppPersona/inicio.html")
      else:
            miFormulario = AlumnoFormulario()
 
      return render(request, "AppPersona/AlumnoFormulario.html", {"miFormulario": miFormulario})

def agregar_adulto1 (request):
 
      if request.method == "POST":
 
            miFormulario = Adulto1Formulario (request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  Adulto1 = Adulto1(nombre=informacion["nombre"],apellido=informacion["apellido"], edad=informacion["edad"], fecha_nac=informacion["fecha"],genero=informacion["genero"],trabajo=informacion["trabajo"],)
                  Adulto1.save()
                  return render(request, "AppPersona/verAlumno.html")
      else:
            miFormulario = Adulto1Formulario()
 
      return render(request, "AppPersona/Adulto1Formulario.html", {"miFormulario": miFormulario})


def agregar_adulto2 (request):
 
      if request.method == "POST":
 
            miFormulario = Adulto2Formulario (request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  Adulto2 = Adulto2(nombre=informacion["nombre"],apellido=informacion["apellido"], edad=informacion["edad"], fecha_nac=informacion["fecha"],genero=informacion["genero"],trabajo=informacion["trabajo"],)
                  Adulto2.save()
                  return render(request, "AppPersona/inicio.html")
      else:
            miFormulario = Adulto2Formulario()
 
      return render(request, "AppPersona/Adulto2Formulario.html", {"miFormulario": miFormulario})

def buscarAlumno(request):
     
     return render (request, "AppPersona/buscarAlumno.html")

def buscarAdulto1(request):
     
     return render (request, "AppPersona/buscarAdulto1.html")

def buscarAdulto2(request):
     
     return render (request, "AppPersona/buscarAdulto2.html")

def resultados(request):
     
     ABusqueda= request.GET["nombre","apellido"]
     resultadosAlumno = Alumno.objects.filter(nombre__icontains=ABusqueda)

     
     return render (request, "AppPersona/resultados.html",{"info1":ABusqueda, "info2":resultadosAlumno})


def resultados1(request):
     
     A1Busqueda= request.GET["nombre","apellido"]
     resultadosAdulto1 = Adulto1.objects.filter(nombre__icontains=A1Busqueda)

     
     return render (request, "AppPersona/resultados1.html",{"info1":A1Busqueda, "info2":resultadosAdulto1})


def resultadosA2(request):
     
     A2Busqueda= request.GET["nombre","apellido"]
     resultadosAdulto2 = Adulto2.objects.filter(nombre__icontains=A2Busqueda)

     
     return render (request, "AppPersona/resultadosA2.html",{"info1":A2Busqueda, "info2":resultadosAdulto2})