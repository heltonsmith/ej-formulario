from django import forms

class SimpleForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    edad = forms.IntegerField()
    email = forms.EmailField()