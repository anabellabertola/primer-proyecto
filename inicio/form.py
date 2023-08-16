from django import forms
from ckeditor.fields import RichTextFormField
from .models import Auto


class AutoFormularioBase(forms.Form):
    class Meta:
        models = Auto
        fields =['nombre', 'marca', 'descripcion', 'imagen', 'fecha_fabricacion']


class CrearAutoFormulario(AutoFormularioBase):
    ...
    
class ModificarAutoFormulario(AutoFormularioBase):
    ...
    
class BuscarAutoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)