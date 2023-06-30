from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('prueba/', views.prueba, name='prueba'),
    path('segunda-vista/', views.segunda_vista, name='segunda-vista'),
    path('fecha-actual/', views.fecha_actual, name='fecha-actual'),
    path('saludar/', views.saludar, name='saludar'),
    path('bienvenida/<str:nombre>/<str:apellido>', views.bienvenida, name='bienvenida'),  
   #v1 crear perro
    #path('crear-perro/<str:nombre>/<int:edad>', views.crear_perro, name='crear-perro'), 
#v2
    path('perros/crear/', views.crear_perro, name='crear_perro'),
    path('perros/', views.listar_perros, name='listar_perros'),
]
