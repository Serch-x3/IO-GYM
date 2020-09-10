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
from django.urls import path,re_path, include
from clients import views
from clients.views import *
from django.conf.urls import url
from clients.filters import *
from django_filters.views import FilterView
from django.contrib.auth.views import LoginView, logout_then_login, PasswordResetDoneView,PasswordResetView, PasswordResetConfirmView,PasswordResetCompleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('admin/graphs/',login_required(views.graphs)),

    path('login/register/', login_required(views.registerUser), name="register"),

    path('reset/password_reset', PasswordResetView.as_view(template_name='login/password_reset_form.html', html_email_template_name="login/password_reset_email.html"), name = 'password_reset'),
    path('reset/password_reset_done', PasswordResetDoneView.as_view(template_name='login/password_reset_done.html'), name = 'password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='login/password_reset_confirm.html'), name = 'password_reset_confirm'),
    path('reset/done',PasswordResetCompleteView.as_view(template_name='login/password_reset_complete.html') , name = 'password_reset_complete'),



    path('accounts/login/', LoginView.as_view(template_name='login/login.html'),name="login index"),
    path('logout/',logout_then_login, name="logout"),


    path('admin/membership/delete/<int:pk>', login_required(MembershipDelete.as_view()),name='create membership'),
    path('admin/membership/index', login_required(MembershipList.as_view(template_name="admin/membership/index.html")),name='index membership'),
    path('admin/membership/index', login_required(GymClassesList.as_view())),
    path('admin/membership/detail/<int:pk>', login_required(MembershipDetails.as_view(template_name="admin/membership/details.html")),name='details membership'),
    path('admin/membership/edit/<int:pk>', login_required(MembershipEdit.as_view(template_name="admin/membership/edit.html")),name='edit membership'),
    path('admin/membership/create', login_required(MembershipCreate.as_view(template_name="admin/membership/create.html")),name='create membership'),

    path('admin/gymclasses/index', login_required(GymClassesList.as_view(template_name = "admin/gymclasses/index.html")), name='index gymclasses'),

    path('admin/gymclasses/delete/<int:pk>', login_required(GymClassesDelete.as_view()),name='delete gymclasses'),

    path('admin/gymclasses/detail/<int:pk>', login_required(GymClassesDetail.as_view(template_name = "admin/gymclasses/detail.html")), name='detail gymclasses'),

    path('admin/gymclasses/edit/<int:pk>', login_required(GymClassesEdit.as_view(template_name = "admin/gymclasses/edit.html")), name='edit gymclasses'),

    path('admin/gymclasses/create', login_required(GymClassesCreate.as_view(template_name = "admin/gymclasses/create.html")), name='create gymclasses'),

    path('admin/groups/index', login_required(GroupsList.as_view(template_name = "admin/groups/index.html")), name='index groups'),

    path('admin/groups/delete/<int:pk>', login_required(GroupsDelete.as_view()),name='gadmin/roups delete'),

    path('admin/groups/detail/<int:pk>', login_required(GroupsDetail.as_view(template_name = "admin/groups/detail.html")), name='detail groups'),

    path('admin/groups/edit/<int:pk>', login_required(GroupsEdit.as_view(template_name = "admin/groups/edit.html")), name='edit groups'),

    path('admin/groups/create', login_required(GroupsCreate.as_view(template_name = "admin/groups/create.html")), name='create groups'),

    path('trainers/', login_required(FilterView.as_view(filterset_class=TrainersFilter,template_name='trainers/index.html')), name='search trainer'),

    path('clients/', login_required(FilterView.as_view(filterset_class=ClientsFilter,template_name='clients/index.html')), name='search client'),

    path('admin/', admin.site.urls),

    path('admin/asistencias/', login_required(FilterView.as_view(filterset_class=ClientsAttendancesFilter,template_name='admin/asistencias.html')), name='search client Attendance'),

    path('admin/asistencias/', clientsView.as_view(template_name = "admin/asistencias.html"), name='admin asistencias'),

    path('admin/index', login_required(trainersAttendance.as_view(template_name = "admin/index.html")), name='admin index'),

    path('trainers/asistencia/checkClientAttendance/<int:pk>', login_required(views.trainerChecking)),

    path('trainers/asistencia/', login_required(FilterView.as_view(filterset_class=TrainersFilter,template_name='trainers/asistencia.html')), name='filter trainer attendance'),

    path('trainers/registros/', login_required(FilterView.as_view(filterset_class=TrainersAttendancesFilter,template_name='trainers/registros.html')), name='search client Attendance'),

    path('trainers/registros/', login_required(trainerAttendanceList.as_view(template_name = "trainers/registros.html")), name='trainers registros'),

    path('trainers/asistencia/', login_required(trainersAttendance.as_view(template_name = "trainers/asistencia.html")), name='trainer asistencia'),

    path('trainers/', login_required(trainersAdministrar.as_view(template_name = "trainers/index.html")), name='trainer administrar'),

    path('trainers/eliminar/<int:pk>', login_required(trainersEliminar.as_view()),name='trainer eliminar'),

    path('trainers/consultar/<int:pk>', login_required(trainersConsulta.as_view(template_name = "trainers/consultar.html")), name='trainer consultar'),

    path('trainers/editar/<int:pk>', login_required(trainersEditar.as_view(template_name = "trainers/editar.html")), name='trainer editar'),

    path('trainers/registrar', login_required(trainersRegistrar.as_view(template_name = "trainers/registrar.html")), name='trainer registrar'),

    path('', login_required(FilterView.as_view(filterset_class=ClientsFilterForAttendance,template_name='index.html')), name='search client attendance'),

    path('', clientsAttendances.as_view(template_name = "index.html"), name='index'),

    path('checkClientAttendance/<int:pk>', login_required(views.clientChecking)),

    # La ruta 'leer' en donde listamos todos los registros o clients de la Base de Datos
    path('clients/', login_required(clientsListado.as_view(template_name = "clients/index.html")), name='leer'),

    # La ruta 'detalles' en donde mostraremos una página con los detalles de un postre o registro
    path('clients/detalle/<int:pk>', login_required(clientsDetalle.as_view(template_name = "clients/detalles.html")), name='detalles'),

    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo postre o registro
    path('clients/crear', login_required(clientsCrear.as_view(template_name = "clients/crear.html")), name='crear'),

    path('clients/crear/membership/<int:pk>', login_required(MembershipEditFromCreate.as_view(template_name = "admin/membership/editfromcreate.html")), name='membership from create'),

    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un postre o registro de la Base de Datos
    path('clients/editar/<int:pk>', login_required(clientsActualizar.as_view(template_name = "clients/actualizar.html")), name='actualizar'),

    # La ruta 'eliminar' que usaremos para eliminar un postre o registro de la Base de Datos
    path('clients/eliminar/<int:pk>', login_required(clientsEliminar.as_view()), name='eliminar'),
]
