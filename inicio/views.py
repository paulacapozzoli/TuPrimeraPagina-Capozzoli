from django.shortcuts import render
from django.http import HttpResponse

# vista inicio
def inicio(request):
    return HttpResponse('Es el inicio')
