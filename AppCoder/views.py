from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import loader
from AppCoder.models import Familiar

import datetime

# Create your views here.

def inicio(request):
    return render(request,'AppCoder/inicio.html')

def Paises(request):
    return render(request,'AppCoder/paises.html')

def Empresas(request):
    return render(request,'AppCoder/empresas.html')

def Autos(request):
    return render(request,'AppCoder/autos.html')
