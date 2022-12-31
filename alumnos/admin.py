from django.contrib import admin
from django import forms
from .models import Alumnos, Inasistencias, Cursos, models
# Register your models here.

class BinaryFileInput(forms.ClearableFileInput):

    def is_initial(self, value):
        return bool(value)
    
    def format_value(self, value):
        if self.is_initial(value):
            return f'{len(value)} bytes'    
    
    def value_from_datadict(self, data, files, name):
        upload = super().value_from_datadict(data, files, name)
        if upload:
            return upload.read()

class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.BinaryField: {'widget':BinaryFileInput()}
    }

@admin.register(Alumnos)
class AlumnosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'curso')
    ordering = ('apellidos', 'nombre')
    list_display_links = ('nombre',)
    search_fields = ('apellidos', 'nombre', 'dni')
    list_filter = ('sexo', 'curso')
    #exclude = ('dni',)
    list_per_page = 5

@admin.register(Cursos)
class CursosAdmin(admin.ModelAdmin):
    list_display = ('año', 'division')
    list_filter = ('division',)
    ordering = ('-año', 'division')
    exclude = ('año', 'division')


@admin.register(Inasistencias)
class InasistenciasAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'fecha')
    ordering = ('fecha', 'alumno')
    list_per_page = 10
    search_fields = ('alumno',)