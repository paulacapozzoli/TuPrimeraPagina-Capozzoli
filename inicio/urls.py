from django.urls import path
from inicio.views import inicio, listado_de_plantas, registrar_planta

urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('plantas/', listado_de_plantas, name='listado_de_plantas'),
    path('plantas/registrar/', registrar_planta, name='registrar_planta'),
]
