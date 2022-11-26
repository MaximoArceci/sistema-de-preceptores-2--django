from rest_framework import serializers
from .models import Alumnos, Cursos, Inasistencias

class AlumnosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumnos
        fields = ('dni', 'nombre', 'apellidos', 'fecha_nacimiento', 'sexo', 'curso')

class CursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cursos
        fields = ("año", "division")

class InasistenciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cursos
        fields = ("fecha", "justificada", "alumno", "tarde")