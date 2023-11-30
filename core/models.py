from django.db import models
from django.contrib.auth.models import User

class Requisito(models.Model):
    requisito = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    atributo = models.ForeignKey('Atributo', on_delete=models.CASCADE, related_name='requisitos')

    def __str__(self):
        return f"Requisito {self.requisito}"

class Producto(models.Model):
    producto = models.AutoField(primary_key=True)
    proyecto = models.ForeignKey('Proyecto', on_delete=models.CASCADE, related_name='productos')
    nombre_producto = models.CharField(max_length=150)
    objetivo_producto = models.TextField()
    tipo_producto = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_producto

class Proyecto(models.Model):
    id_proyecto = models.AutoField(primary_key=True)
    requisito = models.ForeignKey(Requisito, on_delete=models.CASCADE, related_name='proyectos')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre_proyecto = models.CharField(max_length=150)
    fecha_proyecto = models.DateField()

    def __str__(self):
        return self.nombre_proyecto

class Subcaracteristica(models.Model):
    caracteristica = models.ForeignKey('Caracteristica', on_delete=models.CASCADE, related_name='subcaracteristicas')
    subcaracteristica = models.AutoField(primary_key=True)
    nombre_subcaracteristica = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre_subcaracteristica} ({self.caracteristica})"

class Caracteristica(models.Model):
    caracteristica = models.AutoField(primary_key=True)
    nombre_caracteristica = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_caracteristica

class Resultado(models.Model):
    evaluacion = models.ForeignKey('Evaluacion', on_delete=models.CASCADE, related_name='resultados')
    resultado = models.AutoField(primary_key=True)
    resultado_nom = models.CharField(max_length=255)
    atributo = models.ForeignKey('Atributo', on_delete=models.CASCADE, related_name='resultados')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return f'Resultado {self.resultado} - Evaluacion: {self.evaluacion}, Atributo: {self.atributo}, Producto: {self.producto}'

class Informe(models.Model):
    resultado = models.ForeignKey(Resultado, on_delete=models.CASCADE, related_name='informes')
    evaluacion = models.ForeignKey('Evaluacion', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    informe = models.AutoField(primary_key=True)
    informe_recomendaciones = models.TextField()
    informe_general = models.TextField()
    informe_detallado = models.TextField()

    def __str__(self):
        return f'Informe {self.informe} - Resultado: {self.resultado}, Evaluacion: {self.evaluacion}, Producto: {self.producto}'

class Ponderacion(models.Model):
    evaluacion = models.ForeignKey('Evaluacion', on_delete=models.CASCADE, related_name='ponderaciones')
    ponderacion = models.AutoField(primary_key=True)
    ponderado = models.DecimalField(max_digits=5, decimal_places=2)
    ponderado_atributo = models.DecimalField(max_digits=5, decimal_places=2)
    ponderado_subcaracteristica = models.DecimalField(max_digits=5, decimal_places=2)
    ponderado_caracteristica = models.DecimalField(max_digits=5, decimal_places=2)
    atributo = models.ForeignKey('Atributo', on_delete=models.CASCADE, related_name='ponderaciones')

    def __str__(self):
        return f'Ponderacion {self.ponderacion} - Evaluacion: {self.evaluacion}, Atributo: {self.atributo}, Ponderado: {self.ponderado}, Ponderado Atributo: {self.ponderado_atributo}, Ponderado Subcaracteristica: {self.ponderado_subcaracteristica}, Ponderado Caracteristica: {self.ponderado_caracteristica}'

class Evaluacion(models.Model):
    evaluacion = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='evaluaciones')
    riesgo = models.ForeignKey('Riesgo', on_delete=models.CASCADE, related_name='evaluaciones')
    ponderacion = models.ForeignKey(Ponderacion, on_delete=models.CASCADE, related_name='evaluaciones')
    calificacion = models.CharField(max_length=255)

    def __str__(self):
        return f'Evaluacion {self.evaluacion} - Producto: {self.producto}, Riesgo: {self.riesgo}, Ponderacion: {self.ponderacion}, Calificacion: {self.calificacion}'

class Atributo(models.Model):
    atributo = models.AutoField(primary_key=True)
    subcaracteristica = models.ForeignKey(Subcaracteristica, on_delete=models.CASCADE, related_name='atributos')
    caracteristica = models.ForeignKey(Caracteristica, on_delete=models.CASCADE, related_name='atributos')
    nombre_atributo = models.CharField(max_length=255)
    resultado = models.ForeignKey(Resultado, on_delete=models.CASCADE, related_name='atributos')
    requisito = models.ForeignKey(Requisito, on_delete=models.CASCADE, related_name='atributos')
    ponderacion = models.ForeignKey(Ponderacion, on_delete=models.CASCADE, related_name='atributos_ponderacion')

    def __str__(self):
        return f"Atributo {self.nombre_atributo}"

class Riesgo(models.Model):
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE, related_name='riesgos')
    riesgo = models.AutoField(primary_key=True)
    nombre_riesgo = models.CharField(max_length=255)

    def __str__(self):
        return f'Riesgo {self.riesgo} - Evaluacion: {self.evaluacion}, Nombre: {self.nombre_riesgo}'
