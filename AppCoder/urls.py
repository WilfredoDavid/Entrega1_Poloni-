from django.urls import path
from .views import *

urlpatterns = [
    path('', Inicio),
    path('paises', Paises),
    path('empresas', Empresas),
    path('autos', Autos),

]