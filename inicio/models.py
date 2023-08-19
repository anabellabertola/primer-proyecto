from django.db import models
from ckeditor.fields import RichTextField
from django.db import models


class Auto(models.Model):
    nombre = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    descripcion = RichTextField(null=True)
    fecha_fabricacion = models.DateField()
    imagen = models.ImageField(null=True, blank=True, upload_to='imagenes/')
    
    def __str__(self):
        return f"Auto: {self.nombre} - Marca: {self.marca}"
