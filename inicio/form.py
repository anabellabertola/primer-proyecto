from django import forms
from ckeditor.fields import RichTextFormField
from .models import Auto

class AutoFormularioBase(forms.Form):
   nombre = forms.CharField(max_length=20)
   marca = forms.IntegerField()
   descripcion = RichTextFormField()
   fecha_fabricacion = forms.DateField()
   imagen = forms.ImageField()



class CrearAutoFormulario(AutoFormularioBase):
   nombre = forms.CharField(max_length=20)
   marca = forms.IntegerField()
   descripcion = RichTextFormField()
   fecha_fabricacion = forms.DateField()
   imagen = forms.ImageField()
   
class Meta:
    model = Auto
    fields = ['nombre', 'marca', 'descripcion', 'fecha_fabricacion', 'imagen']
    
class ModificarAutoFormulario(AutoFormularioBase):
    ...
    
class BuscarAutoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)