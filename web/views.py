from django.shortcuts import render
from django.http import HttpResponse
from .forms import SimpleForm

# Create your views here.
def hola(request):
    return HttpResponse("hola")

def abrir_formulario(request):
    nombre = None 
    edad = None 

    if request.method == 'POST':
        form = SimpleForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            edad = form.cleaned_data["edad"]
    else:
        form = SimpleForm()

    return render(request, 'formulario.html', {'form': form, 'nombre': nombre, 'edad': edad})