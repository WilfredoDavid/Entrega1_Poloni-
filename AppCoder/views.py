from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import loader
from AppCoder.forms import *
from AppCoder.models import *

import datetime

# Create your views here.

def Inicio(request):
    return render(request,'AppCoder/inicio.html')

def Paises(request):
    return render(request,'AppCoder/paises.html')

def Empresas(request):
    return render(request,'AppCoder/empresas.html')

def Autos(request):
    return render(request,'AppCoder/autos.html')

def autoFormulario(request):

    if request.method =='POST':

        Formulario_auto = AutoFormulario(request.POST)
    
        print(Formulario_auto)

        if Formulario_auto.is_valid:

             informacion = Formulario_auto.cleaned_data 
             auto = Autos (marca=informacion['marca'], modelo =informacion['modelo'], anio_lanzamiento = informacion['anio_lanzamiento'])
             auto.save()
        
             return render(request, "AppCoder/inicio.html",{'mensaje':'datos cargados'})

    else:

        Formulario_auto= AutoFormulario()

    return render(request, "AppCoder/Formulario_auto.html",{"Formulario_auto":Formulario_auto})

def autoFormularioBusq(request):

    return render(request, "AppCoder/autoFormularioBusq.html")

def buscar(request):
    if request.GET['modelo']:
        modelo=request.GET["modelo"]
        autos=Autos.objects.filter(modelo=modelo)
        if len(autos)!=0:
             return render(request, "Appcoder/resultadoBusqueda.html",{"autos":autos})
        else:
             return render(request, "Appcoder/resultadoBusqueda.html",{"mensaje":"No hay autos del modelo ingresado"})
    else:
       return render(request, "Appcoder/resultadoBusqueda.html",{"mensaje":"No se ingreso datos"})

