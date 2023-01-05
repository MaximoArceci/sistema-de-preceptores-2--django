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

class AlumnosPicture(models.Model):
    bytes = models.TextField()
    filename = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=50)

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
            print(self.imagen.url)
            print(type(self.binario))
            print("________________________")
            url = (self.imagen.url)[1:]
            imagen_decode = open(url, "wb")
            print("________________________")
            imagen_decode.write(base64.b64decode(self.binario))
            print("________________________")
            imagen_decode.close()
            return mark_safe(f'<img src = "{self.imagen.url}" width = "200" height="200"/>')
        except:pass
    


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

