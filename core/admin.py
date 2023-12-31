from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_superuser')  
    search_fields = ('username', 'email')  

    

admin.site.unregister(User)  # Desregistrar el UserAdmin predeterminado
admin.site.register(User, CustomUserAdmin)  # Registrar tu CustomUserAdmin
