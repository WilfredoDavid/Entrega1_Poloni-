from django import forms

class AutoFormulario(forms.Form):
    marca = forms.CharField()
    modelo = forms.CharField()
    anio_lanzamiento = forms.IntegerField()