from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from clients.forms import *
import locale


from django.urls import reverse
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Count
from django import forms
from django.views import View
from .filters import *
from datetime import datetime, timedelta
from django.http import HttpResponseRedirect

def graphs(request):
    
    general = GeneralStats.objects.first()
    generalStats = [general.clients, general.trainers, general.groups,general.classes,general.active_memberships,general.expirated_memberships]

    cflm = CFLM.objects.first()
    CFLMData = [cflm.sunday,cflm.monday,cflm.tuesday,cflm.wednesday,cflm.thursday,cflm.friday,cflm.saturday]

    cfl3m = CFL3M.objects.first()
    CFL3MData = [cfl3m.sunday,cfl3m.monday,cfl3m.tuesday,cfl3m.wednesday,cfl3m.thursday,cfl3m.friday,cfl3m.saturday]

    cfl6m = CFL6M.objects.first()
    CFL6MData = [cfl6m.sunday,cfl6m.monday,cfl6m.tuesday,cfl6m.wednesday,cfl6m.thursday,cfl6m.friday,cfl6m.saturday]

    cfly = CFLY.objects.first()
    CFLYData = [cfly.sunday,cfly.monday,cfly.tuesday,cfly.wednesday,cfly.thursday,cfly.friday,cfly.saturday]

    hclyd = HCLYD.objects.first()
    HCLYDData = [hclyd.sunday,hclyd.monday,hclyd.tuesday,hclyd.wednesday,hclyd.thursday,hclyd.friday,hclyd.saturday]

    cflym = CFLYM.objects.values_list()
    CFLYMData = []
    CFLYMLabels = []
    for c in cflym:
        CFLYMData.append(c[1])
        CFLYMLabels.append(c[2] + ' ' + str(c[3]))

    hcfm = HCFM.objects.values_list()
    HCFMData = []
    HCFMLabels = []
    for c in hcfm:
        HCFMData.append(c[1])
        HCFMLabels.append(c[2] + ' ' + str(c[3]))

    nclym = NCLYM.objects.values_list()
    NCLYMData = []
    NCLYMLabels = []

    for c in nclym:
        NCLYMData.append(c[1])
        NCLYMLabels.append(c[2] + ' ' + str(c[3]))

    print("--------------------------------------------------")
    print(NCLYMData)
    print("--------------------------------------------------")

    return render(request,'admin/graphs/index.html',{
        'general': generalStats,
        'CFLM': CFLMData,
        'CFL3M': CFL3MData,
        'CFL6M': CFL6MData,
        'CFLY': CFLYData,
        'HCLYD': HCLYDData,
        'CFLYMData': CFLYMData,
        'CFLYMLabels': CFLYMLabels,
        'HCFMData': HCFMData,
        'HCFMLabels': HCFMLabels,
        'NCLYMData': NCLYMData,
        'NCLYMLabels': NCLYMLabels
    })


def attendance2admin(request):
    return render(request,'login/attendance2admin.html',{})

def admin2attendance(request):
    return render(request,'login/admin2attendance.html',{})

class RegisterLoginView(View):
    def get(self, request):
        return render(request, 'login/create.html', { 'form': UserCreationForm() })

    def post(self, request):
        form = UserCreationForm(request.POST)
        form.is_superuser=True
        form.is_staff=True
        if form.is_valid():
            user = form.save()
            return redirect(reverse('admin index'))

        return render(request, 'login/create.html', { 'form': form })



class trainerAttendanceList(ListView):
    model=trainerAttendanceView

def trainerChecking(request,pk):
    trainer=TRAINERS.objects.get(trainer_id=pk)
    password=request.POST['inputPassword']
    if trainer.trainer_password == password:
        today=datetime.now().date()
        oldAttendance=TRAINERS_ATTENDANCES.objects.filter(trainer_id=pk,date__gte=datetime.now().replace(hour=0,minute=0,second=0).date())
        print(oldAttendance.count())
        print(today)
        if (oldAttendance.count()%2)==0 or (oldAttendance.count()==0):
            attendance=TRAINERS_ATTENDANCES(trainer_id=TRAINERS(trainer_id=pk), description="Entrada")
            messages.add_message(request, messages.SUCCESS, 'Ingreso exitoso. ¡Bienvenido!')
        else:
            attendance=TRAINERS_ATTENDANCES(trainer_id=TRAINERS(trainer_id=pk), description="Salida")
            messages.add_message(request, messages.SUCCESS, 'Salida exitosa. ¡Hasta luego!')
        attendance.save()
    else:
        messages.add_message(request, messages.ERROR, 'Contraseña incorrecta. Intente de nuevo')

    return redirect('trainer asistencia')

def clientChecking(request,pk):
    client=MEMBERSHIPS.objects.get(client_id=pk)
    if datetime.now().date() <= client.expiration_date:
        attendance=CLIENTS_ATTENDANCES(client_id=CLIENTS(client_id=pk))
        attendance.save()
        advice=''
        daysleft= (client.expiration_date - datetime.now().date()).days
        if daysleft == 0:
            advice='Recuerda: ¡Hoy se vence tu membresía!'
            messages.add_message(request, messages.INFO, 'Ingreso exitoso. ¡Bienvenido!' + "\n" + advice)
        else:
            advice=' Tu membresía se vence en: '+ str(daysleft)+ " días."
            messages.add_message(request, messages.SUCCESS, 'Ingreso exitoso. ¡Bienvenido!' + "\n" + advice)
    else:
        messages.add_message(request, messages.ERROR, '¡Ingreso erróneo!. Membresia vencida')

    return redirect("index")

class MembershipList(ListView):
    model=MEMBERSHIPS

class MembershipDelete(SuccessMessageMixin, DeleteView):
    model = MEMBERSHIPS
    form = MEMBERSHIPS
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = '¡Entrenador eliminado correctamente!' # Mostramos este Mensaje luego de Editar un Postre
        messages.success (self.request, (success_message))
        return reverse('index membership') # Redireccionamos a la vista principal 'leer'

class MembershipDetails(DetailView):
    model=MEMBERSHIPS

class MembershipEditFromCreate(SuccessMessageMixin,UpdateView):
    form_class = MembershipForm
    model = MEMBERSHIPS
    success_message = 'Cliente registrado correctamente !' # Mostramos este Mensaje luego de Editar un Postre

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class MembershipEdit(SuccessMessageMixin,UpdateView):
    form_class = MembershipForm
    model = MEMBERSHIPS
    success_message = '¡Membresía actualizada correctamente!' # Mostramos este Mensaje luego de Editar un Postre

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('index membership') # Redireccionamos a la vista principal 'leer'

class MembershipCreate(SuccessMessageMixin,CreateView):
    form_class = MembershipForm
    model = MEMBERSHIPS
    success_message = '¡Membresía creada correctamente!' # Mostramos este Mensaje luego de Crear un Postre

    # Redireccionamos a la página principal luego de crear un registro o postre
    def form_valid(self, form):
        data = form.save()  # save form
        return redirect('edit membership', pk=data.membership_id)

class GymClassesList(ListView):
    model=GYMCLASSES

class GymClassesDelete(SuccessMessageMixin, DeleteView):
    model = GYMCLASSES
    form = GYMCLASSES
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = '¡Clase eliminada correctamente!' # Mostramos este Mensaje luego de Editar un Postre
        messages.success (self.request, (success_message))
        return reverse('index gymclasses') # Redireccionamos a la vista principal 'leer'


class GymClassesEdit(SuccessMessageMixin, UpdateView):
    model = GYMCLASSES
    form = GYMCLASSES
    fields = "__all__"
    success_message = '¡Clase actualizada correctamente!' # Mostramos este Mensaje luego de Editar un Postre

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('index gymclasses') # Redireccionamos a la vista principal 'leer'

class GymClassesDetail(DetailView):
    model=GYMCLASSES

class GymClassesCreate(SuccessMessageMixin, CreateView):
    model = GYMCLASSES
    form = GYMCLASSES
    fields = "__all__"
    success_message = '¡Clase creada correctamente!' # Mostramos este Mensaje luego de Crear un Postre

    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):
        return reverse('index gymclasses') # Redireccionamos a la vista principal 'leer'

class GroupsList(ListView):
    model=GROUPS

class GroupsDelete(SuccessMessageMixin, DeleteView):
    model = GROUPS
    form = GROUPS
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = '¡Grupo eliminado correctamente!' # Mostramos este Mensaje luego de Editar un Postre
        messages.success (self.request, (success_message))
        return reverse('index groups') # Redireccionamos a la vista principal 'leer'


class GroupsEdit(SuccessMessageMixin, UpdateView):
    model = GROUPS
    form = GROUPS
    fields = "__all__"
    success_message = '¡Grupo actualizado correctamente!' # Mostramos este Mensaje luego de Editar un Postre


    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('index groups') # Redireccionamos a la vista principal 'leer'

class GroupsDetail(DetailView):
    model=GROUPS

class GroupsCreate(SuccessMessageMixin, CreateView):
    model = GROUPS
    form = GROUPS
    fields = "__all__"
    success_message = '¡Grupo creado correctamente!' # Mostramos este Mensaje luego de Crear un Postre

    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):
        return reverse('index groups') # Redireccionamos a la vista principal 'leer'


class clientsView(ListView):
    model=clientesView

class trainersAttendance(ListView):
    model=TRAINERS

class trainersAdministrar(ListView):
    model=TRAINERS

class trainersEliminar(SuccessMessageMixin, DeleteView):
    model = TRAINERS
    form = TRAINERS
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = '¡Entrenador eliminado correctamente!' # Mostramos este Mensaje luego de Editar un Postre
        messages.success (self.request, (success_message))
        return reverse('trainer administrar') # Redireccionamos a la vista principal 'leer'


class trainersEditar(SuccessMessageMixin, UpdateView):
    model = TRAINERS
    form_class = trainerForm
    success_message = '¡Entrenador actualizado correctamente!' # Mostramos este Mensaje luego de Editar un Postre

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('trainer administrar') # Redireccionamos a la vista principal 'leer'

class trainersConsulta(DetailView):
    model=TRAINERS

class trainersRegistrar(SuccessMessageMixin, CreateView):
    model = TRAINERS
    form_class = trainerForm
    success_message = '¡Entrenador registrado correctamente!' # Mostramos este Mensaje luego de Crear un Postre

    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):
        return reverse('trainer administrar') # Redireccionamos a la vista principal 'leer'

class clientsAttendances(ListView):
    model=CLIENTS


class clientsListado(ListView):
    model = CLIENTS

class clientsDetalle(DetailView):
    model = CLIENTS

class clientsCrear(SuccessMessageMixin, CreateView):
    model = CLIENTS
    form = CLIENTS
    fields = "__all__"
    success_message = '¡Cliente registrado correctamente!' # Mostramos este Mensaje luego de Crear un Postre

    # Redireccionamos a la página principal luego de crear un registro o postre

    def form_valid(self, form):
        data = form.save()  # save form
        membership=MEMBERSHIPS(client_id=CLIENTS(client_id=data.client_id))
        membership.save()
        return redirect('membership from create', pk=membership.membership_id)

class clientsActualizar(SuccessMessageMixin, UpdateView):
    model = CLIENTS
    form = CLIENTS
    fields = "__all__"
    success_message = '¡Cliente actualizado correctamente!' # Mostramos este Mensaje luego de Editar un Postre

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class clientsEliminar(SuccessMessageMixin, DeleteView):
    model = CLIENTS
    form = CLIENTS
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = '¡Cliente eliminado correctamente!' # Mostramos este Mensaje luego de Editar un Postre
        messages.success (self.request, (success_message))
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
