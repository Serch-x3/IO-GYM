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

    #HOME
    #path('', login_required(FilterView.as_view(filterset_class=ClientsFilter,template_name='index.html')), name='search client attendance'),
    #path('', clientsAttendances.as_view(template_name = "index.html"), name='index'),
    path('', login_required(views.clientsAttendancesPages), name='index'),
    path('admin/', admin.site.urls),
    path('admin/index', login_required(trainersAttendance.as_view(template_name = "admin/index.html")), name='admin index'),


    #STADISTICS
    path('admin/graphs/',login_required(views.graphs), name = 'graphs'),


    #USER CRUD
    path('user/index/', login_required(UserList.as_view(template_name = "users/index.html")), name="user index"),
    path('user/create/', login_required(views.UserCreate), name="user create"),
    path('user/delete/<int:pk>', login_required(views.UserDelete.as_view()),name='user delete'),
    path('user/edit/<int:pk>', login_required(views.EditUser),name='user edit'),
    path('user/details/<int:pk>', login_required(UserDetail.as_view()),name='user details'),


    #USER ACCOUNTS LOGIN MANAGMENT
    path('reset/password_reset', PasswordResetView.as_view(template_name='login/password_reset_form.html', html_email_template_name="login/password_reset_email.html"), name = 'password_reset'),
    path('reset/password_reset_done', PasswordResetDoneView.as_view(template_name='login/password_reset_done.html'), name = 'password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='login/password_reset_confirm.html'), name = 'password_reset_confirm'),
    path('reset/done',PasswordResetCompleteView.as_view(template_name='login/password_reset_complete.html') , name = 'password_reset_complete'),
    path('accounts/login/', LoginView.as_view(template_name='login/login.html'),name="login index"),
    path('logout/',logout_then_login, name="logout"),


    #MEMBERSHIPS
    path('admin/memberships/', login_required(MembershipList.as_view(template_name="admin/membership/index.html")),name='index membership'),
    #path('admin/memberships/create', login_required(MembershipCreate.as_view(template_name="admin/membership/create.html")),name='create membership'),
    path('admin/memberships/details/<int:pk>', login_required(MembershipDetails.as_view(template_name="admin/membership/details.html")),name='details membership'),
    path('admin/memberships/edit/<int:pk>', login_required(MembershipEdit.as_view(template_name="admin/membership/edit.html")),name='edit membership'),
    #path('admin/memberships/delete/<int:pk>', login_required(MembershipDelete.as_view()),name='create membership'),


    #GYMCLASSES
    path('admin/gymclasses/', login_required(GymClassesList.as_view(template_name = "admin/gymclasses/index.html")), name='index gymclasses'),
    path('admin/gymclasses/create', login_required(GymClassesCreate.as_view(template_name = "admin/gymclasses/create.html")), name='create gymclasses'),
    path('admin/gymclasses/detail/<int:pk>', login_required(GymClassesDetail.as_view(template_name = "admin/gymclasses/detail.html")), name='detail gymclasses'),
    path('admin/gymclasses/edit/<int:pk>', login_required(GymClassesEdit.as_view(template_name = "admin/gymclasses/edit.html")), name='edit gymclasses'),
    path('admin/gymclasses/delete/<int:pk>', login_required(GymClassesDelete.as_view()),name='delete gymclasses'),

    #GROUPS
    path('admin/groups/index', login_required(GroupsList.as_view(template_name = "admin/groups/index.html")), name='index groups'),
    path('admin/groups/create', login_required(GroupsCreate.as_view(template_name = "admin/groups/create.html")), name='create groups'),
    path('admin/groups/detail/<int:pk>', login_required(GroupsDetail.as_view(template_name = "admin/groups/detail.html")), name='detail groups'),
    path('admin/groups/edit/<int:pk>', login_required(GroupsEdit.as_view(template_name = "admin/groups/edit.html")), name='edit groups'),
    path('admin/groups/delete/<int:pk>', login_required(GroupsDelete.as_view()),name='delete groups'),



    #TRAINERS
    #path('trainers/', login_required(FilterView.as_view(filterset_class=TrainersFilter,template_name='trainers/index.html')), name='search trainer'),
    #path('trainers/', login_required(TrainerList.as_view(template_name = "trainers/index.html")), name='trainer index'),
    path('trainers/', login_required(views.TrainerListPages), name='trainer index'),
    path('trainers/create', login_required(TrainerCreate.as_view(template_name = "trainers/create.html")), name='trainer create'),
    path('trainers/delete/<int:pk>', login_required(TrainerDelete.as_view()), name='trainer delete'),
    path('trainers/edit/<int:pk>', login_required(TrainerEdit.as_view(template_name = "trainers/edit.html")), name='trainer edit'),
    path('trainers/details/<int:pk>', login_required(TrainerDetails.as_view(template_name = "trainers/details.html")), name='trainer details'),
    #TRAINER ATTENDANCES
    #path('trainers/attendances/', login_required(FilterView.as_view(filterset_class=TrainersAttendancesFilter, template_name='trainers/attendances.html')), name='search trainer Attendance'),
    #path('trainers/attendances/', trainerAttendanceList.as_view(template_name = "trainers/attendances.html"), name='trainer attendances'),
    path('trainers/attendances/', login_required(views.trainerAttendanceListPages), name='trainer attendances'),
    #TRAINER ATTENDANCE MODE
    #path('trainers/attendancemode/', login_required(FilterView.as_view(filterset_class=TrainersFilter,template_name='trainers/attendanceMode.html')), name='filter trainer attendance'),
    #path('trainers/attendancemode/', login_required(trainersAttendance.as_view(template_name = "trainers/attendanceMode.html")), name='trainer attendance mode'),
    path('trainers/attendancemode/', login_required(views.trainersAttendancePages), name='trainer attendance mode'),
    path('trainers/attendancemode/checkClientAttendance/<int:pk>', login_required(views.trainerChecking), name = 'trainer check'),


    #CLIENTS
    #path('clients/', login_required(FilterView.as_view(filterset_class=ClientsFilter,template_name='clients/index.html')), name='search client'),
    #path('clients/', login_required(ClientList.as_view(template_name = "clients/index.html")), name='client index'),
    path('clients/', login_required(views.ClientListPages), name='client index'),
    path('clients/create', login_required(ClientCreate.as_view(template_name = "clients/create.html")), name='client create'),
    path('clients/create/membership/<int:pk>', login_required(MembershipEditFromCreate.as_view(template_name = "admin/membership/editfromcreate.html")), name='edit membership from create'),
    path('clients/delete/<int:pk>', login_required(ClientDelete.as_view()), name='client delete'),
    path('clients/editar/<int:pk>', login_required(ClientEdit.as_view(template_name = "clients/edit.html")), name='client edit'),
    path('clients/detalle/<int:pk>', login_required(ClientDetails.as_view(template_name = "clients/details.html")), name='client details'),
    #CLIENT ATTENDANCES
    #path('clients/attendances/', login_required(FilterView.as_view(filterset_class=ClientsAttendancesFilter,template_name='clients/attendances.html')), name='search client Attendance'),
    #path('clients/attendances/', clientAttendanceList.as_view(template_name = "clients/attendances.html"), name='client attendances'),
    path('clients/attendances/', login_required(views.clientAttendanceListPages), name='client attendances'),
    #path('clients/attendances/', views.clientsView, name = "client attendances"),
    path('checkClientAttendance/<int:pk>', login_required(views.clientChecking), name = 'client check'),
    path('checkClientAttendanceByRFID', login_required(views.clientCheckingByRFID), name = 'client check with rfid')
]
