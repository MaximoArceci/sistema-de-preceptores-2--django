from rest_framework import serializers
from .models import Alumnos

class AlumnosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumnos
        fields = ('dni', 'nombre', 'apellidos', 'fecha_nacimiento', 'sexo', 'curso')