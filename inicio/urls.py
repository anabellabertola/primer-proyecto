from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('acerca_de_mi/', views.acerca_de_mi, name='acerca_de_mi'),
    path('primer-vista/', views.primer_vista, name='primer-vista'),
    path('fecha-actual/', views.fecha_actual, name='fecha-actual'),
    path('saludar/', views.saludar, name='saludar'),
    path('bienvenida/<str:nombre>/<str:apellido>', views.bienvenida, name='bienvenida'),  
   
    path('autos/', views.ListarAutos.as_view(), name='listar_autos'),
    path('autos/crear/', views.CrearAuto.as_view(), name='crear_auto'),
    path('autos/eliminar/<int:pk>/', views.EliminarAuto.as_view(), name='eliminar_auto'),
    path('autos/modificar/<int:pk>/', views.ModificarAuto.as_view(), name='modificar_auto'),
    path('autos/<int:pk>/', views.MostrarAuto.as_view(), name='mostrar_auto'),
]