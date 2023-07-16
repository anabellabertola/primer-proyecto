from django.db import models
from ckeditor.fields import RichTextField

class Auto(models.Model):
    nombre = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    descripcion = RichTextField(null=True)
    
    def __str__(self):
        return f"Auto: {self.nombre} - Marca: {self.marca}"