# En core/urls.py

from django.urls import path
from . import views
from .views import inicio_sesion, registro, principal, MisProyectosView



urlpatterns = [
    path('', views.inicio, name='inicio'),  # Ruta para la vista de inicio
    path('inicio-sesion/', inicio_sesion, name='inicio_sesion'),
    path('registro/', registro, name='registro'),
    path('principal/', principal, name='principal'),
    path('mis_proyectos/', MisProyectosView.as_view(), name='mis_proyectos'),
]
