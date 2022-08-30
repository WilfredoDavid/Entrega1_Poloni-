from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import loader
from AppCoder.models import Familiar

import datetime

# Create your views here.

def inicio(request):
    return HttpResponse('vista inicio')

def Paises(request):
    return HttpResponse('vista paises')

def Empresas(request):
    return HttpResponse('vista empresas')

def Autos(request):
    return HttpResponse('vista autos')