from django.contrib import admin
from .models import Alumnos, Inasistencias, Cursos
# Register your models here.

@admin.register(Alumnos)
class AlumnosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'curso', 'admin_photo')
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