from .models import Alumnos
from rest_framework import viewsets, permissions
from .serializers import AlumnosSerializer
class AlumnosViewSet(viewsets.ModelViewSet):
    queryset = Alumnos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AlumnosSerializer 