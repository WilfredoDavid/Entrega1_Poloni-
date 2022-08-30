from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import loader
from AppCoder.models import Familiar

import datetime

# Create your views here.

#Se crea la funcion para instanciar familia

def familia(self):
    #Información "De Entrada"
    hoy= datetime.date.today()
    index=[0,1,2,3]
    lista_parentescos=['Referencia','Padre','Madre','Hermano']
    lista_nombres=['Yamil', 'Sergio', 'Norma', 'Diego']
    lista_apellidos=['Poloni', 'Poloni', 'Woelke', 'Battisti']
    lista_fechas_nacimiento=[datetime.date(1993,12,22), datetime.date(1947,1,2), datetime.date(1955,4,1), datetime.date(1978,9,6)]
    lista_edad=[]
    nota=['Los partescos son relativos a persona referencia','','','']
    #Procesamiento de la información 
    for i in lista_fechas_nacimiento:
        if ((hoy.month-i.month)>=0 and (hoy.day-i.day>0)):
            lista_edad.append(hoy.year-i.year)
        else:
            lista_edad.append(hoy.year-i.year-1)

    #Instanciamiento de la clases, con lo cual se puede guardar la información según APP        
    
    familiares=[]
    for i in index:
        instancia=Familiar(nombre=lista_nombres[i],apellido=lista_apellidos[i],parentesco=lista_parentescos[i],fecha_de_nacimiento=lista_fechas_nacimiento[i],edad=lista_edad[i],nota=nota[i])
      
        familiares.append(instancia)


    #Se pasa la información al diccionario para poder mostrarlo con la plantilla
    diccionario= {"Nombres":lista_nombres, "Apellidos":lista_apellidos, "Parentescos": lista_parentescos,"Fechas_de_Nacimiento": lista_fechas_nacimiento, "Edades":lista_edad, "Nota": nota}

    plantilla =loader.get_template('template1.html')

    #Se guarda la informacion instanciada en la base de datos
    for i in familiares:
       i.save()

    #Se renderiza y se devuelve el documento
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)