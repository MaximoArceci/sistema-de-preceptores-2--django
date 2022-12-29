from django.db import models
from .choices import sexos, cursos
from django.utils.safestring import mark_safe

class Cursos(models.Model):
    año = models.CharField(max_length=1)
    division = models.CharField(max_length=1)

    def __str__(self):
        return str(self.año) + str(self.division)

class Alumnos(models.Model):
    dni = models.IntegerField()
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=70)
    fecha_nacimiento = models.DateField(verbose_name="fecha de nacimiento")
    sexo = models.CharField(max_length=1, choices=sexos, default="X")
    curso = models.ForeignKey(Cursos, null=True, blank=True, on_delete=models.CASCADE)
    foto = models.ImageField(null=True, blank=True)

    def admin_photo(self):
        try:
            return mark_safe('<img src="{}" width="100" />'.format(self.foto.url))
        except:
            return self.foto


    def nombre_completo(self):
        return"{}, {}".format(self.apellidos, self.nombre)
    
    def __str__(self):
        return self.nombre_completo() + " - " + str(self.curso)

    class Meta():
        ordering= ['apellidos', 'nombre']
        

class Inasistencias(models.Model):
    fecha = models.DateField()
    justificada = models.BooleanField(default=False)
    alumno = models.ForeignKey(Alumnos, null=True, blank=True, on_delete=models.CASCADE)
    tarde = models.BooleanField(default=False)

    def __str__(self):
        return str(self.fecha) + " - " + str(self.alumno)

