from django.urls import path, include
from .views import hola, abrir_formulario

urlpatterns = [
    path("", hola, name="inicio"),
    path("abrir/", abrir_formulario, name="abrir"),
]