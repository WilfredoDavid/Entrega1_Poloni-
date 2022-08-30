from django.http import HttpResponse
from django.template import Context, Template, loader

def probandoTemplate(request):
    nom= "Yamil"
    ape= "Poloni"
    diccionario = {"nombre": nom, "apellido": ape}
    plantilla = loader.get_template("template1.html")
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)