from django.db import models
from django.contrib.auth.models import User

class Requisitos(models.Model):
    nombre = models.CharField(max_length=255)
    

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    

    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    id_proyecto = models.AutoField(primary_key=True)
    requisitos = models.ForeignKey(Requisitos, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    nombre_proyecto = models.CharField(max_length=150)
    fecha_proyecto = models.DateField()
    estado_proyecto = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre_proyecto

