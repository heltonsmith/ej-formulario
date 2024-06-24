from django.contrib import admin
from .models import Persona

# Register your models here.
@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'edad', 'email')
    search_fields = ('nombre', 'email')