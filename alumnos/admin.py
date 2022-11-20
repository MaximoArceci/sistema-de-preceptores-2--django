from django.contrib import admin
from .models import Alumnos, Inasistencias, Cursos
# Register your models here.

admin.site.register(Alumnos)
admin.site.register(Inasistencias)
admin.site.register(Cursos)