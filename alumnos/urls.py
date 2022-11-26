from django.urls import path
from . import views
from .api import AlumnosViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('api/alumnos', AlumnosViewSet, 'alumnos')

#urlpatterns = [
#    path('', views.index),
#    path('cursos/<str:curso>', views.pagCurso),
#]

urlpatterns = router.urls