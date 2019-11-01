"""IOGYM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from clients.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('trainers/asistencia', trainersAsistencia.as_view(template_name = "trainers/asistencia.html"), name='trainer asistencia'),

    path('trainers/', trainersAdministrar.as_view(template_name = "trainers/index.html"), name='trainer administrar'),

    path('trainers/eliminar/<int:pk>', trainersEliminar.as_view(),name='trainer eliminar'),

    path('trainers/consultar/<int:pk>', trainersConsulta.as_view(template_name = "trainers/consultar.html"), name='trainer consultar'),

    path('trainers/editar/<int:pk>', trainersEditar.as_view(template_name = "trainers/editar.html"), name='trainer editar'),

    path('trainers/registrar', trainersRegistrar.as_view(template_name = "trainers/registrar.html"), name='trainer registrar'),

    path('', clientsAttendancesCrear.as_view(template_name = "index.html"), name='index'),

    # La ruta 'leer' en donde listamos todos los registros o clients de la Base de Datos
    path('clients/', clientsListado.as_view(template_name = "clients/index.html"), name='leer'),

    # La ruta 'detalles' en donde mostraremos una página con los detalles de un postre o registro
    path('clients/detalle/<int:pk>', clientsDetalle.as_view(template_name = "clients/detalles.html"), name='detalles'),

    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo postre o registro
    path('clients/crear', clientsCrear.as_view(template_name = "clients/crear.html"), name='crear'),

    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un postre o registro de la Base de Datos
    path('clients/editar/<int:pk>', clientsActualizar.as_view(template_name = "clients/actualizar.html"), name='actualizar'),

    # La ruta 'eliminar' que usaremos para eliminar un postre o registro de la Base de Datos
    path('clients/eliminar/<int:pk>', clientsEliminar.as_view(), name='eliminar'),
]
