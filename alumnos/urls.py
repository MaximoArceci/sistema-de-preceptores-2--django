from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('quintoA/', views.quintoA),
    path('quintoB/', views.quintoB),
    path('cuartoA/', views.cuartoA),
    path('cuartoB/', views.cuartoB),
    path('terceroA/', views.terceroA),
    path('terceroB/', views.terceroB),
    path('segundoA/', views.segundoA),
    path('segundoB/', views.segundoB),
    path('primeroA/', views.primeroA),
    path('primeroB/', views.primeroB),
]