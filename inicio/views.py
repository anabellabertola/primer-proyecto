from typing import Any, Dict
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from inicio.models import Auto
from django.shortcuts import render, redirect
from inicio.form import CrearAutoFormulario, BuscarAutoFormulario, ModificarAutoFormulario
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def acerca_de_mi(request):
    
    segundos = datetime.now().second
    diccionario = {
        'mensaje': 'Mi nombre de Anabella Bertola,soy alumna de CoderHouse, tengo 28 años y vivo en Rosario.Esta es una pagina informativa a traves de listado de autos alta gama de distintas marcas y modelos, donde podran ver mas informacion de la descripcion',
    }
    
    return render(request, 'inicio/acerca_de_mi.html', diccionario)


def inicio(request):
 return render(request, 'inicio/inicio.html')

def primer_vista(request):
    return HttpResponse('<h1>Soy la primer vista</h1>')

def fecha_actual(request):
    fecha = datetime.now()
    return HttpResponse(f'<h1>Fecha actual: {fecha}</h1>')

def saludar(request):
    return HttpResponse('Bienvenido/a!!!')

def bienvenida(request, nombre, apellido):
    return HttpResponse(f'Bienvenido/a {nombre.title()} {apellido.title()}!!!')

def listar_autos(request):
    formulario = BuscarAutoFormulario(request.GET)
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data['nombre']
        listado_de_autos = Auto.objects.filter(nombre__icontains=nombre_a_buscar)
        
    formulario = BuscarAutoFormulario()        
    return render(request, 'inicio/listar_autos.html', {'formulario': formulario, 'autos': listado_de_autos})
  
def eliminar_auto(request, auto_id):
    
    auto = Auto.objects.get(id=auto_id)
    auto.delete()
    
    return redirect('inicio:listar_autos')

def modificar_auto(request, auto_id):
    auto_a_modificar = Auto.objects.get(id=auto_id)               
  
    if request.method == 'POST':
        formulario = ModificarAutoFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            auto_a_modificar.nombre = info['nombre']
            auto_a_modificar.marca = info['marca']
            auto_a_modificar.imagen = info['imagen']
            auto_a_modificar.fecha_fabricacion['fecha_fabricacion']
            auto_a_modificar.save()
            return redirect('inicio:listar_autos')
        else:
            return render(request, 'inicio/modificar_auto.html', {'formulario': formulario})
    
    formulario = ModificarAutoFormulario(initial={'nombre': auto_a_modificar.nombre, 'marca': auto_a_modificar.marca, 'imagen': auto_a_modificar.imagen, 'fecha_fabricacion': auto_a_modificar.fecha_fabricacion})
    return render(request, 'inicio/modificar_auto.html', {'formulario': formulario})


class CrearAuto(CreateView):
    model = Auto
    template_name = 'inicio/CBV/crear_auto_CBV.html'
    fields = ['nombre', 'marca', 'descripcion', 'imagen', 'fecha_fabricacion']
    success_url = reverse_lazy('inicio:listar_autos')
    
class ListarAutos(ListView):
    model = Auto
    template_name = "inicio/CBV/listar_autos_CBV.html"
    context_object_name = 'autos'
    
    def get_queryset(self):
        listado_de_autos = []
        formulario = BuscarAutoFormulario(self.request.GET)
        if formulario.is_valid():
            nombre_a_buscar = formulario.cleaned_data['nombre']
            listado_de_autos = Auto.objects.filter(nombre__icontains=nombre_a_buscar)
        return listado_de_autos
    
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)   
        contexto['formulario'] = BuscarAutoFormulario()
        return contexto
    
    
class ModificarAuto(LoginRequiredMixin, UpdateView):
    model = Auto
    template_name = "inicio/CBV/modificar_auto_CBV.html"
    fields = ['nombre', 'marca', 'descripcion', 'imagen', 'fecha_fabricacion']
    success_url = reverse_lazy('inicio:listar_autos')
      
class EliminarAuto(LoginRequiredMixin, DeleteView):
    model = Auto
    template_name = "inicio/CBV/eliminar_auto_CBV.html"
    success_url = reverse_lazy('inicio:listar_autos')

class MostrarAuto(DetailView):
    model = Auto
    template_name = "inicio/CBV/mostrar_auto_CBV.html"

