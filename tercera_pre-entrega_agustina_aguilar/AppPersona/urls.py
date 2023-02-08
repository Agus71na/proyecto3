from django.urls import path
from AppPersona.views import *

urlpatterns = [
    path('Alumnos/', ver_alumno),
    path('Adulto1/', ver_adulto1),
    path('Adulto2/', ver_adulto2),
    path('nuevoAlumno/', agregar_alumno),
    path('nuevoAdulto1/', agregar_adulto1),
    path('nuevoAdulto2/', agregar_adulto2),
    path('buscarAlumno/', buscarAlumno),
    path('buscarAdulto1/', buscarAdulto1),
    path('buscarAdulto2/', buscarAdulto2),
    path('resultados/', resultados),
    path('resultados1/', resultados1),
    path('resultadosA2/', resultadosA2),

]
