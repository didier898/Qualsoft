# En tu archivo forms.py
from django import forms

class ObjetivoForm(forms.Form):
    objetivos_descripcion = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}), required=True)

class CrearProyectoForm(forms.Form):
    nombre_proyecto = forms.CharField(max_length=150, required=True)
    fecha_proyecto = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), required=True)
    nombre_producto = forms.CharField(max_length=150, required=True)
    
class IdentificarProductoForm(forms.Form):
    CHOICES = [('intermedio', 'Producto Intermedio'), ('final', 'Producto Final')]
    tipo_producto = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    
    
class RequisitoForm(forms.Form):
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}), required=True)