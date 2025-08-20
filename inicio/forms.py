from django import forms

class FormularioRegistrarPlanta(forms.Form):
    especie = forms.CharField(max_length=25)
    habitat = forms.CharField(max_length=18)