from django.urls import path, include
from .views import hola, abrir_formulario, agregar_persona, lista_personas

urlpatterns = [
    path("", hola, name="inicio"),
    path("abrir/", abrir_formulario, name="abrir"),
    path("agregar/", agregar_persona, name="agregar"),
    path("listar/", lista_personas, name="listar"),
]