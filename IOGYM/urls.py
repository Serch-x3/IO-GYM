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
from  clients import views
from clients.views import *
from django.conf.urls import url
from clients.filters import *
from django_filters.views import FilterView

urlpatterns = [
    path('admin/membership/delete/<int:pk>', MembershipDelete.as_view(),name='create membership'),
    path('admin/membership/index', MembershipList.as_view(template_name="admin/membership/index.html"),name='index membership'),
    path('admin/membership/index', GymClassesList.as_view()),
    path('admin/membership/detail/<int:pk>', MembershipDetails.as_view(template_name="admin/membership/details.html"),name='details membership'),
    path('admin/membership/edit/<int:pk>', MembershipEdit.as_view(template_name="admin/membership/edit.html"),name='edit membership'),
    path('admin/membership/create', MembershipCreate.as_view(template_name="admin/membership/create.html"),name='create membership'),

    path('admin/gymclasses/index', GymClassesList.as_view(template_name = "admin/gymclasses/index.html"), name='index gymclasses'),

    path('admin/gymclasses/delete/<int:pk>', GymClassesDelete.as_view(),name='delete gymclasses'),

    path('admin/gymclasses/detail/<int:pk>', GymClassesDetail.as_view(template_name = "admin/gymclasses/detail.html"), name='detail gymclasses'),

    path('admin/gymclasses/edit/<int:pk>', GymClassesEdit.as_view(template_name = "admin/gymclasses/edit.html"), name='edit gymclasses'),

    path('admin/gymclasses/create',GymClassesCreate.as_view(template_name = "admin/gymclasses/create.html"), name='create gymclasses'),

    path('admin/groups/index', GroupsList.as_view(template_name = "admin/groups/index.html"), name='index groups'),

    path('admin/groups/delete/<int:pk>', GroupsDelete.as_view(),name='gadmin/roups delete'),

    path('admin/groups/detail/<int:pk>', GroupsDetail.as_view(template_name = "admin/groups/detail.html"), name='detail groups'),

    path('admin/groups/edit/<int:pk>', GroupsEdit.as_view(template_name = "admin/groups/edit.html"), name='edit groups'),

    path('admin/groups/create',GroupsCreate.as_view(template_name = "admin/groups/create.html"), name='create groups'),

    path('admin/hours/create', hoursCreate.as_view(template_name = "admin/hours/create.html"), name='create hours'),

    path('admin/hours/delete/<int:pk>', hoursDelete.as_view(),name='delete hours'),

    path('admin/hours/index', hoursView.as_view(template_name="admin/hours/index.html"), name='index hours'),

    path('admin/weekdays/create', weekdaysCreate.as_view(template_name = "admin/weekdays/create.html"), name='create weekdays'),

    path('admin/weekdays/delete/<int:pk>', weekdayDelete.as_view(),name='delete weekays'),

    path('admin/weekdays/index', weekdaysView.as_view(template_name="admin/weekdays/index.html"), name='index weekdays'),

    path('trainers/', FilterView.as_view(filterset_class=TrainersFilter,template_name='trainers/index.html'), name='search trainer'),

    path('clients/', FilterView.as_view(filterset_class=ClientsFilter,template_name='clients/index.html'), name='search client'),

    path('admin/', admin.site.urls),

    path('admin/asistencias/', FilterView.as_view(filterset_class=ClientsAttendancesFilter,template_name='admin/asistencias.html'), name='search client Attendance'),

    path('admin/asistencias/', clientsView.as_view(template_name = "admin/asistencias.html"), name='admin asistencias'),

    path('admin/index', trainersAttendance.as_view(template_name = "admin/index.html"), name='admin index'),

    path('trainers/asistencia/checkClientAttendance/<int:pk>', views.trainerChecking),

    path('trainers/asistencia/', FilterView.as_view(filterset_class=TrainersFilter,template_name='trainers/asistencia.html'), name='filter trainer attendance'),

    path('trainers/registros/', FilterView.as_view(filterset_class=TrainersAttendancesFilter,template_name='trainers/registros.html'), name='search client Attendance'),

    path('trainers/registros/', trainerAttendanceList.as_view(template_name = "trainers/registros.html"), name='trainers registros'),

    path('trainers/asistencia/', trainersAttendance.as_view(template_name = "trainers/asistencia.html"), name='trainer asistencia'),

    path('trainers/', trainersAdministrar.as_view(template_name = "trainers/index.html"), name='trainer administrar'),

    path('trainers/eliminar/<int:pk>', trainersEliminar.as_view(),name='trainer eliminar'),

    path('trainers/consultar/<int:pk>', trainersConsulta.as_view(template_name = "trainers/consultar.html"), name='trainer consultar'),

    path('trainers/editar/<int:pk>', trainersEditar.as_view(template_name = "trainers/editar.html"), name='trainer editar'),

    path('trainers/registrar', trainersRegistrar.as_view(template_name = "trainers/registrar.html"), name='trainer registrar'),

    path('', FilterView.as_view(filterset_class=ClientsFilterForAttendance,template_name='index.html'), name='search client attendance'),

    path('', clientsAttendances.as_view(template_name = "index.html"), name='index'),

    path('checkClientAttendance/<int:pk>', views.clientChecking),

    # La ruta 'leer' en donde listamos todos los registros o clients de la Base de Datos
    path('clients/', clientsListado.as_view(template_name = "clients/index.html"), name='leer'),

    # La ruta 'detalles' en donde mostraremos una página con los detalles de un postre o registro
    path('clients/detalle/<int:pk>', clientsDetalle.as_view(template_name = "clients/detalles.html"), name='detalles'),

    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo postre o registro
    path('clients/crear', clientsCrear.as_view(template_name = "clients/crear.html"), name='crear'),

    path('clients/crear/membership/<int:pk>', MembershipEditFromCreate.as_view(template_name = "admin/membership/editfromcreate.html"), name='membership from create'),

    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un postre o registro de la Base de Datos
    path('clients/editar/<int:pk>', clientsActualizar.as_view(template_name = "clients/actualizar.html"), name='actualizar'),

    # La ruta 'eliminar' que usaremos para eliminar un postre o registro de la Base de Datos
    path('clients/eliminar/<int:pk>', clientsEliminar.as_view(), name='eliminar'),
]
