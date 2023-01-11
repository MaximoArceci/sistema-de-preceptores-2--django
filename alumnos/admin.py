from django.contrib import admin
from db_file_storage.form_widgets import DBAdminClearableFileInput
from django import forms
import os
from .models import Alumnos, Inasistencias, Cursos, models
from django.utils.safestring import mark_safe
# Register your models here.

"""class BinaryFileInput(forms.ClearableFileInput):

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
    }"""

"""class AlumnosForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        exclude = []
        widgets = {
            'picture': DBAdminClearableFileInput
        }

class ConsoleAdmin(admin.ModelAdmin):
    form = AlumnosForm"""

@admin.register(Alumnos)
class AlumnosAdmin(admin.ModelAdmin):
    readonly_fields = ["admin_photo"]
    list_display = ('nombre', 'apellidos', 'curso', 'admin_photo')
    ordering = ('apellidos', 'nombre')
    list_display_links = ('nombre',)
    search_fields = ('apellidos', 'nombre', 'dni')
    list_filter = ('sexo', 'curso')
    exclude = ('user', 'binario')
    list_per_page = 5

""" @mark_safe
    def alumno_imagen(self, obj):
        try:
            print(obj)
            print("------> IMAGEN", str(obj.imagen))
            return f'<img src="{str(obj.imagen)}" height="{obj.imagen.height}" width="{obj.imagen.width}" />'
        except:
            
            obj.imagen = "photos/login_logo.png"
            return f'<img src="photos/login_logo.png" height="200px" width="200px" />'"""

@admin.register(Cursos)
class CursosAdmin(admin.ModelAdmin):
    list_display = ('año', 'division')
    list_filter = ('division',)
    ordering = ('-año', 'division')
    #exclude = ('año', 'division')


@admin.register(Inasistencias)
class InasistenciasAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'fecha')
    ordering = ('fecha', 'alumno')
    list_per_page = 10
    search_fields = ('alumno',)