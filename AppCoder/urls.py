from django.urls import path
from .views import *

urlpatterns = [
    path('', Inicio, name= 'inicio'),
    path('paises', Paises, name='paises'),
    path('empresas', Empresas, name='empresas'),
    path('autos', Autos, name='autos'),
    path('autoFormulario', autoFormulario, name='AutoFormulario1'),

]