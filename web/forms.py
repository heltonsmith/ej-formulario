from django import forms
from .models import Persona

class SimpleForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    edad = forms.IntegerField()
    email = forms.EmailField()

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'edad', 'email']