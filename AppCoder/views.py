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
             auto = Auto (marca=informacion['marca'], modelo =informacion['modelo'], anio_lanzamiento = informacion['anio_lanzamiento'])
             auto.save()
        
             return render(request, "AppCoder/inicio.html")

    else:

        Formulario_auto= AutoFormulario()
    
    return render(request, "AppCoder/Formulario_auto.html",{"Formulario_auto":Formulario_auto})