from .models import Alumnos, Cursos, Inasistencias
from rest_framework import viewsets, permissions
from .serializers import AlumnosSerializer, CursosSerializer, InasistenciasSerializer
import django_filters.rest_framework

class AlumnosViewSet(viewsets.ModelViewSet):
    queryset = Alumnos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AlumnosSerializer 
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['dni', 'nombre', 'apellidos', 'fecha_nacimiento', 'sexo', 'curso']

class CursosViewSet(viewsets.ModelViewSet):
    queryset = Cursos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CursosSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['año', 'division']

class InasistenciasViewSet(viewsets.ModelViewSet):
    queryset = Inasistencias.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = InasistenciasSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['fecha', 'justificada', 'alumno', 'tarde']  