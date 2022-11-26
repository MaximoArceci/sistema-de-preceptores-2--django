from .models import Alumnos, Cursos, Inasistencias
from rest_framework import viewsets, permissions
from .serializers import AlumnosSerializer, CursosSerializer, InasistenciasSerializer

class AlumnosViewSet(viewsets.ModelViewSet):
    queryset = Alumnos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AlumnosSerializer 

class CursosViewSet(viewsets.ModelViewSet):
    queryset = Cursos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CursosSerializer

class InasistenciasViewSet(viewsets.ModelViewSet):
    queryset = Inasistencias.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = InasistenciasSerializer