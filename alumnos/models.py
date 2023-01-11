from django.db import models
from .choices import sexos, cursos
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
import pathlib
import base64

class Cursos(models.Model):
    año = models.CharField(max_length=1)
    division = models.CharField(max_length=1)

    def __str__(self):
        return str(self.año) + str(self.division)
        

class Alumnos(models.Model):
    def generarUsuario(self):
        #DECODE
        imagen = "URL"
        return imagen

    dni = models.IntegerField()
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=70)
    fecha_nacimiento = models.DateField(verbose_name="fecha de nacimiento")
    sexo = models.CharField(max_length=1, choices=sexos, default="X")
    curso = models.ForeignKey(Cursos, null=True, blank=True, on_delete=models.CASCADE)
    imagen = models.ImageField(blank=True, null=True, upload_to="fotos/") #(upload_to='alumnos.AlumnosPicture/bytes/mimetype/filename', blank=True, null=True)
    binario = models.BinaryField(blank=True, null=True, editable=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def admin_photo(self):
        try:
            if len(self.binario) < 10:
                return mark_safe(f'<img src = "/media/no_borrar/no_image.jpeg" width = "100" height="100"/>')
            tipoD = str(self.imagen).split(".")
            return mark_safe(f'<img style="width:100px;height:100px"; src="data:image/{tipoD[-1]};base64,{str(self.binario)[2:-1]}">')
            
        except:
            return mark_safe(f'<img src = "/media/no_borrar/no_image.jpeg" width = "100" height="100"/>')
    


    def nombre_completo(self):
        return"{}, {}, {}".format(self.apellidos, self.nombre, self.dni)
    
    def __str__(self):
        return self.nombre_completo() #+ " - " + str(self.curso)

    class Meta():
        ordering= ['apellidos', 'nombre']
        

class Inasistencias(models.Model):
    fecha = models.DateField()
    justificada = models.BooleanField(default=False)
    alumno = models.ForeignKey(Alumnos, null=True, blank=True, on_delete=models.CASCADE)
    tarde = models.BooleanField(default=False)

    def __str__(self):
        return str(self.fecha) + " - " + str(self.alumno)

