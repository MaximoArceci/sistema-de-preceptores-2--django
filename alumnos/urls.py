from django.urls import path
from . import views
from .api import AlumnosViewSet, CursosViewSet, InasistenciasViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('api/alumnos', AlumnosViewSet, 'alumnos')
router.register('api/cursos', CursosViewSet, 'cursos')
router.register('api/inasistencias', InasistenciasViewSet, 'inasistencias')

#urlpatterns = [
#    path('', views.index),
#    path('cursos/<str:curso>', views.pagCurso),
#]

urlpatterns = router.urls