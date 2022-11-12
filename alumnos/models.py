from django.db import models
from .choices import sexos, cursos
# Create your models here.

class Alumnos(models.Model):
    dni = models.IntegerField()
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=70)
    fecha_nacimiento = models.DateField(verbose_name="fecha de nacimiento")
    sexo = models.CharField(max_length=1, choices=sexos, default="X")
    curso = models.CharField(max_length=2, choices=cursos)

    def nombre_completo(self):
        return"{}, {}".format(self.apellidos, self.nombre)
    
    def __str__(self):
        return self.nombre_completo() + " - " + self.curso

    class Meta():
        ordering= ['apellidos', 'nombre']
        

class Inasistencias(models.Model):
    fecha = models.DateField()
    justificada = models.BooleanField(default=False)
    alumno = models.ForeignKey(Alumnos, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.fecha, self.alumno

