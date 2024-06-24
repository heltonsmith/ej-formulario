from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SimpleForm, PersonaForm
from .models import Persona

# Create your views here.
def hola(request):
    return HttpResponse("hola")

def abrir_formulario(request):
    nombre = None 
    edad = None 
    email = None

    if request.method == 'POST':
        form = SimpleForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            edad = form.cleaned_data["edad"]
            email = form.cleaned_data["email"]
    else:
        form = SimpleForm()

    return render(request, 'formulario.html', {'form': form, 'nombre': nombre, 'edad': edad, 'email': email})

def agregar_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = PersonaForm()
    
    return render(request, 'form_persona.html', {'form': form})

def lista_personas(request):
    personas = Persona.objects.all()
    return render(request, 'listar.html', {'personas': personas})