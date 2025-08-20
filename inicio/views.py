from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Planta
from inicio.forms import FormularioRegistrarPlanta

# vista inicio
def inicio(request):

    return render(request, 'inicio.html')

#vista registrar_planta
def registrar_planta(request):

    print(request.POST)

    if request.method == "POST":

        formulario = FormularioRegistrarPlanta(request.POST)

        if formulario.is_valid():
            info = formulario.cleaned_data
            
            planta = Planta(especie=info.get('especie'), habitat=info.get('habitat'))
            planta.save()

            return redirect('listado_de_plantas')
    
    else:
        
        formulario = FormularioRegistrarPlanta()

    return render(request, 'registrar_planta.html', {'formulario':formulario})

def listado_de_plantas(request):

    plantas = Planta.objects.all()

    return render(request, 'listado_de_plantas.html', {'plantas':plantas})