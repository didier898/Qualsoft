# En tu archivo forms.py
from django import forms

class ObjetivoDescripcionForm(forms.Form):
    objetivos_descripcion = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}))
