from django import forms
from ckeditor.fields import RichTextFormField
from .models import Auto


class AutoFormularioBase(forms.Form):
   nombre = forms.CharField(max_length=20)
   marca = forms.IntegerField()
   descripcion = RichTextFormField()
   imagen = forms.ImageField()
   fecha_fabricacion = forms.DateField()


class CrearAutoFormulario(AutoFormularioBase):
    ...
    
class ModificarAutoFormulario(AutoFormularioBase):
    ...
    
class BuscarAutoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)