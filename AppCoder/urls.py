from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio),
    path('paises', views.Paises, name="Paises"),
    path('empresas', views.Empresas),
    path('autos', views.Autos),


]