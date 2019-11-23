from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from clients.forms import *

from django.urls import reverse
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django import forms
from .filters import *
from datetime import datetime, timedelta
from django.http import HttpResponseRedirect


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
        success_message = 'Entrenador Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre
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
    success_message = 'Membresía actualizada correctamente !' # Mostramos este Mensaje luego de Editar un Postre

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('index membership') # Redireccionamos a la vista principal 'leer'

class MembershipCreate(SuccessMessageMixin,CreateView):
    form_class = MembershipForm
    model = MEMBERSHIPS
    success_message = 'Entrenador Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre

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
        success_message = 'Clase eliminada correctamente' # Mostramos este Mensaje luego de Editar un Postre
        messages.success (self.request, (success_message))
        return reverse('index gymclasses') # Redireccionamos a la vista principal 'leer'


class GymClassesEdit(SuccessMessageMixin, UpdateView):
    model = GYMCLASSES
    form = GYMCLASSES
    fields = "__all__"
    success_message = 'Clase actualizada correctamente' # Mostramos este Mensaje luego de Editar un Postre

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('index gymclasses') # Redireccionamos a la vista principal 'leer'

class GymClassesDetail(DetailView):
    model=GYMCLASSES

class GymClassesCreate(SuccessMessageMixin, CreateView):
    model = GYMCLASSES
    form = GYMCLASSES
    fields = "__all__"
    success_message = 'Clase creada correctamente' # Mostramos este Mensaje luego de Crear un Postre

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
        success_message = 'Grupo eliminado correctamente' # Mostramos este Mensaje luego de Editar un Postre
        messages.success (self.request, (success_message))
        return reverse('index groups') # Redireccionamos a la vista principal 'leer'


class GroupsEdit(SuccessMessageMixin, UpdateView):
    model = GROUPS
    form = GROUPS
    fields = "__all__"
    success_message = 'Grupo actualizado correctamente' # Mostramos este Mensaje luego de Editar un Postre

    def form_valid(self, form):
        day=form.data.get('day')
        hour=form.data.get('hour')
        minutes=form.data.get('minutes')
        print(type(minutes))
        ampm=form.data.get('ampm')
        weekdays=WEEKDAYS.objects.get_or_create(weekdays_name=day)
        s=str(hour)+':'+str(minutes)+' '+str(ampm)
        hours=HOURS.objects.get_or_create(hour_name=s)
        group=GROUPS(trainer_id=TRAINERS(trainer_id=form.data.get('trainer_id')), gymclass_id= GYMCLASSES(gymclass_id=form.data.get('gymclass_id')), weekday_id=WEEKDAYS.objects.get(weekdays_name=day), hour_id=HOURS.objects.get(hour_name=s))
        group.save()
        return redirect('index groups')

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('index groups') # Redireccionamos a la vista principal 'leer'

class GroupsDetail(DetailView):
    model=GROUPS

class GroupsCreate(SuccessMessageMixin, CreateView):
    model = GROUPS
    form = GROUPS
    fields = "__all__"
    success_message = 'Grupo creado correctamente' # Mostramos este Mensaje luego de Crear un Postre

    def form_valid(self, form):
        day=form.data.get('day')
        hour=int(form.data.get('hour'))
        if hour <10:
            hour='0'+str(hour)
        minutes=int(form.data.get('minutes'))
        if minutes <10:
            minutes='0'+str(minutes)
        ampm=form.data.get('ampm')
        weekdays=WEEKDAYS.objects.get_or_create(weekdays_name=day)
        s=str(hour)+':'+str(minutes)+' '+str(ampm)
        hours=HOURS.objects.get_or_create(hour_name=s)
        group=GROUPS(trainer_id=TRAINERS(trainer_id=form.data.get('trainer_id')), gymclass_id= GYMCLASSES(gymclass_id=form.data.get('gymclass_id')), weekday_id=WEEKDAYS.objects.get(weekdays_name=day), hour_id=HOURS.objects.get(hour_name=s))
        group.save()
        return redirect('index groups')

    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):
        return reverse('index groups') # Redireccionamos a la vista principal 'leer'


class hoursCreate(SuccessMessageMixin, CreateView):
    model = HOURS
    form = HOURS
    fields = "__all__"
    success_message = 'Hora creada correctamente' # Mostramos este Mensaje luego de Crear un Postre

    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):
        return reverse('index hours') # Redireccionamos a la vista principal 'leer'

class hoursDelete(SuccessMessageMixin, DeleteView):
    model = HOURS
    form = HOURS
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = 'Hora eliminada correctamente' # Mostramos este Mensaje luego de Editar un Postre
        messages.success (self.request, (success_message))
        return reverse('index hours') # Redireccionamos a la vista principal 'leer'

class hoursView(ListView):
    model= HOURS

class weekdaysCreate(SuccessMessageMixin, CreateView):
    model = WEEKDAYS
    form = WEEKDAYS
    fields = "__all__"
    success_message = 'Día creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre

    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):
        return reverse('index weekdays') # Redireccionamos a la vista principal 'leer'

class weekdayDelete(SuccessMessageMixin, DeleteView):
    model = WEEKDAYS
    form = WEEKDAYS
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = 'Día eliminado correctamente' # Mostramos este Mensaje luego de Editar un Postre
        messages.success (self.request, (success_message))
        return reverse('index weekdays') # Redireccionamos a la vista principal 'leer'

class weekdaysView(ListView):
    model= WEEKDAYS

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
        success_message = 'Entrenador Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre
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
    success_message = 'Entrenador creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre

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
    success_message = 'Cliente Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre

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
    success_message = 'Cliente Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class clientsEliminar(SuccessMessageMixin, DeleteView):
    model = CLIENTS
    form = CLIENTS
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = 'Cliente Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre
        messages.success (self.request, (success_message))
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
