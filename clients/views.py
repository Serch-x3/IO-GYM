from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *

from django.urls import reverse

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django import forms

class trainersAsistencia(SuccessMessageMixin, CreateView):
    model=TRAINERS_ATTENDANCES
    form=TRAINERS_ATTENDANCES
    fields = "__all__"
    Success_message='Ingreso exitoso'
    def get_success_url(self):
        return reverse('index')

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
    form = TRAINERS
    fields = "__all__"
    success_message = 'Cliente Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('trainer administrar') # Redireccionamos a la vista principal 'leer'

class trainersConsulta(DetailView):
    model=TRAINERS

class trainersRegistrar(SuccessMessageMixin, CreateView):
    model = TRAINERS
    form = TRAINERS
    fields = "__all__"
    success_message = 'Entrenador Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre

    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):
        return reverse('trainer administrar') # Redireccionamos a la vista principal 'leer'

class clientsAttendancesCrear(SuccessMessageMixin, CreateView):
    model=CLIENTS_ATTENDANCES
    form=CLIENTS_ATTENDANCES
    fields = "__all__"
    Success_message='Ingreso exitoso'
    def get_success_url(self):
        return reverse('index')

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
    def get_success_url(self):
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

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
