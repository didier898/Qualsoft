# En Qualsoft/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Incluye las URL de la aplicación 'core'
]
