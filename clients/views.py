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
from django.core.paginator import *


def report(request):

    def changeLanguage(data):
        if "January" in data:
            data = "Enero"
        elif "February" in data:
            data = "Febrero"
        elif "March" in data:
            data = "Marzo"
        elif "April" in data:
            data = "Abril"
        elif "May" in data:
            data = "Mayo"
        elif "June" in data:
            data = "Junio"
        elif "July" in data:
            data = "Julio"
        elif "August" in data:
            data = "Agosto"
        elif "September" in data:
            data = "Septiembre"
        elif "October" in data:
            data = "Octubre"
        elif "November" in data:
            data = "Noviembre"
        elif "December" in data:
            data = "Diciembre"
        return data

    general = GeneralStats.objects.first()
    generalStats = [general.clients, general.trainers, general.classes,
                general.groups, general.active_memberships, general.expirated_memberships]

    cflm = CFLM.objects.first()
    CFLMData = [cflm.sunday, cflm.monday, cflm.tuesday,
                cflm.wednesday, cflm.thursday, cflm.friday, cflm.saturday]

    cfl3m = CFL3M.objects.first()
    CFL3MData = [cfl3m.sunday, cfl3m.monday, cfl3m.tuesday,
                 cfl3m.wednesday, cfl3m.thursday, cfl3m.friday, cfl3m.saturday]

    cfl6m = CFL6M.objects.first()
    CFL6MData = [cfl6m.sunday, cfl6m.monday, cfl6m.tuesday,
                 cfl6m.wednesday, cfl6m.thursday, cfl6m.friday, cfl6m.saturday]

    cfly = CFLY.objects.first()
    CFLYData = [cfly.sunday, cfly.monday, cfly.tuesday,
                cfly.wednesday, cfly.thursday, cfly.friday, cfly.saturday]

    hclyd = HCLYD.objects.first()
    HCLYDData = [hclyd.sunday, hclyd.monday, hclyd.tuesday,
                 hclyd.wednesday, hclyd.thursday, hclyd.friday, hclyd.saturday]

    cflym = CFLYM.objects.values_list()
    CFLYMData = []
    CFLYMLabels = []
    for c in cflym:
        CFLYMData.append(c[1])
        CFLYMLabels.append(changeLanguage(c[2]) + ' ' + str(c[3]))

    hcfm = HCFM.objects.values_list()
    HCFMData = []
    HCFMLabels = []
    for c in hcfm:
        HCFMData.append(c[1])
        HCFMLabels.append(changeLanguage(c[2]) + ' ' + str(c[3]))

    nclym = NCLYM.objects.values_list()
    NCLYMData = []
    NCLYMLabels = []

    for c in nclym:
        NCLYMData.append(c[1])
        NCLYMLabels.append(changeLanguage(c[2]) + ' ' + str(c[3]))

    incomes = IBM.objects.values_list()
    incomesData = []
    incomesLabels = []
    for c in incomes:
        incomesData.append(c[1])
        incomesLabels.append(changeLanguage(c[2]) + " " + str(c[3]))

    sales = MSM.objects.values_list()
    salesData = []
    salesLabels = []
    for c in sales:
        salesData.append(c[1])
        salesLabels.append(changeLanguage(c[2]) + " " + str(c[3]))

    return render(request, 'admin/graphs/report.html', {
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
        'NCLYMLabels': NCLYMLabels,
        'incomesData': incomesData,
        'incomesLabels': incomesLabels,
        'salesData': salesData,
        'salesLabels': salesLabels
    })


def graphs(request):

    def changeLanguage(data):
        if "January" in data:
            data = "Enero"
        elif "February" in data:
            data = "Febrero"
        elif "March" in data:
            data = "Marzo"
        elif "April" in data:
            data = "Abril"
        elif "May" in data:
            data = "Mayo"
        elif "June" in data:
            data = "Junio"
        elif "July" in data:
            data = "Julio"
        elif "August" in data:
            data = "Agosto"
        elif "September" in data:
            data = "Septiembre"
        elif "October" in data:
            data = "Octubre"
        elif "November" in data:
            data = "Noviembre"
        elif "December" in data:
            data = "Diciembre"
        return data

    general = GeneralStats.objects.first()
    generalStats = [general.clients, general.trainers, general.classes,
                general.groups, general.active_memberships, general.expirated_memberships]

    cflm = CFLM.objects.first()
    CFLMData = [cflm.sunday, cflm.monday, cflm.tuesday,
                cflm.wednesday, cflm.thursday, cflm.friday, cflm.saturday]

    cfl3m = CFL3M.objects.first()
    CFL3MData = [cfl3m.sunday, cfl3m.monday, cfl3m.tuesday,
                 cfl3m.wednesday, cfl3m.thursday, cfl3m.friday, cfl3m.saturday]

    cfl6m = CFL6M.objects.first()
    CFL6MData = [cfl6m.sunday, cfl6m.monday, cfl6m.tuesday,
                 cfl6m.wednesday, cfl6m.thursday, cfl6m.friday, cfl6m.saturday]

    cfly = CFLY.objects.first()
    CFLYData = [cfly.sunday, cfly.monday, cfly.tuesday,
                cfly.wednesday, cfly.thursday, cfly.friday, cfly.saturday]

    hclyd = HCLYD.objects.first()
    HCLYDData = [hclyd.sunday, hclyd.monday, hclyd.tuesday,
                 hclyd.wednesday, hclyd.thursday, hclyd.friday, hclyd.saturday]

    cflym = CFLYM.objects.values_list()
    CFLYMData = []
    CFLYMLabels = []
    for c in cflym:
        CFLYMData.append(c[1])
        CFLYMLabels.append(changeLanguage(c[2]) + ' ' + str(c[3]))

    hcfm = HCFM.objects.values_list()
    HCFMData = []
    HCFMLabels = []
    for c in hcfm:
        HCFMData.append(c[1])
        HCFMLabels.append(changeLanguage(c[2]) + ' ' + str(c[3]))

    nclym = NCLYM.objects.values_list()
    NCLYMData = []
    NCLYMLabels = []

    for c in nclym:
        NCLYMData.append(c[1])
        NCLYMLabels.append(changeLanguage(c[2]) + ' ' + str(c[3]))

    incomes = IBM.objects.values_list()
    incomesData = []
    incomesLabels = []
    for c in incomes:
        incomesData.append(c[1])
        incomesLabels.append(changeLanguage(c[2]) + " " + str(c[3]))

    sales = MSM.objects.values_list()
    salesData = []
    salesLabels = []
    for c in sales:
        salesData.append(c[1])
        salesLabels.append(changeLanguage(c[2]) + " " + str(c[3]))

    return render(request, 'admin/graphs/index.html', {
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
        'NCLYMLabels': NCLYMLabels,
        'incomesData': incomesData,
        'incomesLabels': incomesLabels,
        'salesData': salesData,
        'salesLabels': salesLabels
    })


# USER VIEWS
class UserList(ListView):
    model = User


def UserCreate(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, '¡Cuenta creada correctamente!.')
            return redirect('user index')
    else:
        f = CustomUserCreationForm()

    return render(request, 'users/create.html', {'form': f})


class UserDelete(SuccessMessageMixin, DeleteView):
    model = User
    form = User
    fields = "__all__"

    def get_success_url(self):
        success_message = '¡Usuario eliminado correctamente!'
        messages.success(self.request, (success_message))
        return reverse('user index')


def EditUser(request, pk):
    userInfo = []
    userInfo = User.objects.get(pk=pk)

    if request.method == 'GET':
        f = CustomUserEditFormWithPassword()
        return render(request, 'users/edit.html', {'form': f, 'key': pk, 'userInfo': userInfo})

    if request.method == 'POST':

        if request.POST.get('change_password', 'off') == 'on':
            f = CustomUserEditFormWithPassword(request.POST)
        else:
            f = CustomUserEditForm(request.POST)

        if f.is_valid():
            f.save()
            messages.success(request, '¡Cuenta actualizada correctamente!.')
            return redirect('user index')
        else:
            return render(request, 'users/edit.html', {'form': f, 'key': pk, 'userInfo': userInfo})

    else:
        f = CustomUserEditForm()

    return redirect('user index')


class UserEdit(SuccessMessageMixin, UpdateView):
    model = User
    form = CustomUserCreationForm
    fields = ['username', 'email', 'is_superuser']

    def get_object(self, **kwargs):
        return get_object_or_404(self.model, pk=self.kwargs['pk'])

    def get_success_url(self):
        success_message = '¡Usuario actualizado correctamente!'
        messages.success(self.request, (success_message))
        return reverse('user index')


class UserDetail(View):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        userInfo = {
            "user_id": kwargs['pk'],
            "username": user.username,
            "email": user.email,
            "last_login": user.last_login,
            "is_superuser": user.is_superuser
        }
        context = {'userInfo': userInfo}
        return render(request, 'users/details.html', context)


def trainerChecking(request, pk):
    trainer = TRAINERS.objects.get(trainer_id=pk)
    password = request.POST['inputPassword']
    if trainer.trainer_password == password:
        today = datetime.now().date()
        oldAttendance = TRAINERS_ATTENDANCES.objects.filter(
            trainer_id=pk, date__gte=datetime.now().replace(hour=0, minute=0, second=0).date())
        print(oldAttendance.count())
        print(today)
        if (oldAttendance.count() % 2) == 0 or (oldAttendance.count() == 0):
            attendance = TRAINERS_ATTENDANCES(
                trainer_id=TRAINERS(trainer_id=pk), description="Entrada")
            messages.add_message(request, messages.SUCCESS,
                                 'Ingreso exitoso. ¡Bienvenido!')
        else:
            attendance = TRAINERS_ATTENDANCES(
                trainer_id=TRAINERS(trainer_id=pk), description="Salida")
            messages.add_message(request, messages.SUCCESS,
                                 'Salida exitosa. ¡Hasta luego!')
        attendance.save()
    else:
        messages.add_message(request, messages.ERROR,
                             'Contraseña incorrecta. Intente de nuevo')

    return redirect('trainer attendance mode')


def clientCheckingByRFID(request):
    if CLIENTS.objects.filter(client_rfid=request.POST['client_rfid']).exists():
        client = CLIENTS.objects.get(client_rfid=request.POST['client_rfid'])

        membership = MEMBERSHIPS.objects.get(client_id=client.client_id)
        if datetime.now().date() <= membership.expiration_date:
            attendance = CLIENTS_ATTENDANCES(
                client_id=CLIENTS(client_id=client.client_id))
            attendance.save()
            advice = ''
            daysleft = (membership.expiration_date -
                        datetime.now().date()).days
            if daysleft == 0:
                advice = 'Recuerda: ¡Hoy se vence tu membresía!'
                messages.add_message(request, messages.INFO, 'Ingreso exitoso. ¡Bienvenido(a) ' +
                                     client.client_name + ' ' + client.client_surname + '!' + "\n" + advice)
            else:
                advice = ' Tu membresía se vence en: ' + \
                    str(daysleft) + " días."
                messages.add_message(request, messages.SUCCESS, 'Ingreso exitoso. ¡Bienvenido(a) ' +
                                     client.client_name + ' ' + client.client_surname + '!' + "\n" + advice)
        else:
            messages.add_message(request, messages.ERROR,
                                 '¡Ingreso erróneo!. Membresia vencida')

    else:
        messages.add_message(
            request, messages.ERROR, '¡No se ha encontrado algún cliente con esta llave!')

    return redirect('index')


def clientChecking(request, pk):
    client = MEMBERSHIPS.objects.get(client_id=pk)
    if datetime.now().date() <= client.expiration_date:
        attendance = CLIENTS_ATTENDANCES(client_id=CLIENTS(client_id=pk))
        attendance.save()
        advice = ''
        daysleft = (client.expiration_date - datetime.now().date()).days
        client = CLIENTS.objects.get(pk=pk)
        if daysleft == 0:
            advice = 'Recuerda: ¡Hoy se vence tu membresía!'
            messages.add_message(request, messages.INFO, 'Ingreso exitoso. ¡Bienvenido(a) ' +
                                 client.client_name + ' ' + client.client_surname + '!' + "\n" + advice)
        else:
            advice = ' Tu membresía se vence en: ' + str(daysleft) + " días."
            messages.add_message(request, messages.SUCCESS, 'Ingreso exitoso. ¡Bienvenido(a) ' +
                                 client.client_name + ' ' + client.client_surname + '!' + "\n" + advice)
    else:
        messages.add_message(request, messages.ERROR,
                             '¡Ingreso erróneo!. Membresia vencida')

    return redirect("index")



# PAYMENTS VIEW

class PaymentCreate(SuccessMessageMixin, CreateView):
    model = PAYMENTS
    form = PAYMENTS
    fields = "__all__"
    success_message = '¡Pago registrado correctamente!'

    def get_success_url(self):
        return reverse('index payment')


class PaymentList(ListView):
    paginate_by = 25
    model = PAYMENTS


class PaymentEdit(SuccessMessageMixin, UpdateView):
    model = PAYMENTS
    form = PAYMENTS
    fields = "__all__"
    success_message = '¡Pago actualizado correctamente!'

    def get_success_url(self):
        return reverse('index payment')


class PaymentDelete(SuccessMessageMixin, DeleteView):
    model = PAYMENTS
    fields = "__all__"

    def get_success_url(self):
        success_message = '¡Pago eliminado correctamente!'
        messages.success(self.request, (success_message))
        return reverse('index payment')

class PaymentDetails(DetailView):
    model = PAYMENTS




# MEMBERSHIP VIEWS
class MembershipList(ListView):
    paginate_by = 25
    model = MEMBERSHIPS


class MembershipDelete(SuccessMessageMixin, DeleteView):
    model = MEMBERSHIPS
    form = MEMBERSHIPS
    fields = "__all__"

    def get_success_url(self):
        success_message = '¡Entrenador eliminado correctamente!'
        messages.success(self.request, (success_message))
        return reverse('index membership')


class MembershipDetails(DetailView):
    model = MEMBERSHIPS





def membershipEditMethod(request, pk):
    def get_cancel():
        return (datetime.now() - timedelta(days=1)).date()
    def get_days(number):
        return (datetime.now() + timedelta(days=number)).date()
    def get_weeks(number):
        return (datetime.now() + timedelta(weeks=number)).date()
    def get_months(number):
        return (datetime.now() + timedelta(days=number*30)).date()
    def get_years(number):
        return (datetime.now() + timedelta(days=number*365)).date()

    payments = PAYMENTS.objects.all()
    membership = get_object_or_404(MEMBERSHIPS, client_id=pk)
    if request.method == "POST":

        payment_selected = PAYMENTS(number=-1, time_type="Día", payment_description="Default", payment_cost=0)

        request.POST = request.POST.copy()

        if(request.POST.get('payment_option', False)):
            if(not request.POST['payment_option'] == "-1"):
                payment_selected = PAYMENTS.objects.get(pk=request.POST['payment_option'])

                if payment_selected.time_type == 'Día':
                    request.POST['expiration_date'] = get_days(payment_selected.number)
                elif payment_selected.time_type == 'Semana':
                    request.POST['expiration_date'] = get_weeks(payment_selected.number)
                elif payment_selected.time_type == 'Mes':
                    request.POST['expiration_date'] = get_months(payment_selected.number)
                elif payment_selected.time_type == 'Año':
                    request.POST['expiration_date'] = get_years(payment_selected.number)
                request.POST.pop('payment_option')
            else:
                request.POST['expiration_date'] = membership.expiration_date
        else:
            request.POST['expiration_date'] = membership.expiration_date

        form = MembershipForm(request.POST, instance = membership)
        if form.is_valid():
            form.save()
            pay = PAYMENTS_REGISTERS(client_id = CLIENTS(pk=request.POST['client_id']), payment_cost = payment_selected.payment_cost, payment_concept=payment_selected.payment_description)
            pay.save()
            messages.success(request, '¡Membresía actualizada correctamente!')
            return HttpResponseRedirect(reverse('index membership'))

    else:
        form = MembershipForm(request.POST or None, instance=membership)
        f = MembershipForm(request)

    return render(request, 'admin/membership/edit.html', {'form': form, 'payment_options':payments})




def membershipEditFromCreateMethod(request, pk):
    def get_cancel():
        return (datetime.now() - timedelta(days=1)).date()
    def get_days(number):
        return (datetime.now() + timedelta(days=number)).date()
    def get_weeks(number):
        return (datetime.now() + timedelta(weeks=number)).date()
    def get_months(number):
        return (datetime.now() + timedelta(days=number*30)).date()
    def get_years(number):
        return (datetime.now() + timedelta(days=number*365)).date()

    payments = PAYMENTS.objects.all()
    membership = get_object_or_404(MEMBERSHIPS, client_id=pk)
    if request.method == "POST":

        payment_selected = PAYMENTS(number=-1, time_type="Día", payment_description="Default", payment_cost=0)

        request.POST = request.POST.copy()

        if(request.POST.get('payment_option', False)):
            if(not request.POST['payment_option'] == "-1"):
                payment_selected = PAYMENTS.objects.get(pk=request.POST['payment_option'])

                if payment_selected.time_type == 'Día':
                    request.POST['expiration_date'] = get_days(payment_selected.number)
                elif payment_selected.time_type == 'Semana':
                    request.POST['expiration_date'] = get_weeks(payment_selected.number)
                elif payment_selected.time_type == 'Mes':
                    request.POST['expiration_date'] = get_months(payment_selected.number)
                elif payment_selected.time_type == 'Año':
                    request.POST['expiration_date'] = get_years(payment_selected.number)
                request.POST.pop('payment_option')
            else:
                request.POST['expiration_date'] = membership.expiration_date
        else:
            request.POST['expiration_date'] = membership.expiration_date

        form = MembershipForm(request.POST, instance = membership)

        if form.is_valid():
            form.save()
            pay = PAYMENTS_REGISTERS(client_id = CLIENTS(pk=request.POST['client_id']), payment_cost = payment_selected.payment_cost, payment_concept=payment_selected.payment_description)
            pay.save()
            messages.success(request, '¡Cliente registrado correctamente!')
            return HttpResponseRedirect(reverse('client index'))

    else:
        form = MembershipForm(request.POST or None, instance=membership)
        f = MembershipForm(request)

    return render(request, 'admin/membership/edit.html', {'form': form, 'payment_options':payments})




class MembershipEditFromCreate(SuccessMessageMixin, UpdateView):
    form_class = MembershipForm
    model = MEMBERSHIPS
    success_message = 'Cliente registrado correctamente!'

    def get_success_url(self):
        return reverse('client index')


class MembershipEdit(SuccessMessageMixin, UpdateView):
    form_class = MembershipForm
    model = MEMBERSHIPS
    success_message = '¡Membresía actualizada correctamente!'

    def get_success_url(self):
        return reverse('index membership')


class MembershipCreate(SuccessMessageMixin, CreateView):
    form_class = MembershipForm
    model = MEMBERSHIPS
    success_message = '¡Membresía creada correctamente!'

    def form_valid(self, form):
        data = form.save()
        return redirect('edit membership', pk=data.membership_id)


# GYMCLASS VIEWS
class GymClassesList(ListView):
    paginate_by = 25
    model = GYMCLASSES


class GymClassesDelete(SuccessMessageMixin, DeleteView):
    model = GYMCLASSES
    form = GYMCLASSES
    fields = "__all__"

    def get_success_url(self):
        success_message = '¡Clase eliminada correctamente!'
        messages.success(self.request, (success_message))
        return reverse('index gymclasses')


class GymClassesEdit(SuccessMessageMixin, UpdateView):
    model = GYMCLASSES
    form = GYMCLASSES
    fields = "__all__"
    success_message = '¡Clase actualizada correctamente!'

    def get_success_url(self):
        return reverse('index gymclasses')


class GymClassesDetail(DetailView):
    model = GYMCLASSES


class GymClassesCreate(SuccessMessageMixin, CreateView):
    model = GYMCLASSES
    form = GYMCLASSES
    fields = "__all__"
    success_message = '¡Clase creada correctamente!'

    def get_success_url(self):
        return reverse('index gymclasses')


# GROUP VIEWS
class GroupsList(ListView):
    paginate_by = 25
    model = GROUPS


class GroupsDelete(SuccessMessageMixin, DeleteView):
    model = GROUPS
    form = GROUPS
    fields = "__all__"

    def get_success_url(self):
        success_message = '¡Grupo eliminado correctamente!'
        messages.success(self.request, (success_message))
        return reverse('index groups')


class GroupsEdit(SuccessMessageMixin, UpdateView):
    model = GROUPS
    form = GROUPS
    fields = "__all__"
    success_message = '¡Grupo actualizado correctamente!'

    def get_success_url(self):
        return reverse('index groups')


class GroupsDetail(DetailView):
    model = GROUPS


class GroupsCreate(SuccessMessageMixin, CreateView):
    model = GROUPS
    form = GROUPS
    fields = "__all__"
    success_message = '¡Grupo creado correctamente!'

    def get_success_url(self):
        return reverse('index groups')


# ATTENDANCE
class clientAttendanceList(ListView):
    model = clientAttendanceView


def clientAttendanceListPages(request):
    qs = clientAttendanceView.objects.all().order_by('-date')
    object_list = ClientsAttendancesFilter(request.GET, queryset=qs).qs
    page_obj = Paginator(object_list, 25)
    page = request.GET.get('page')
    filter_instance = {}
    try:
        page_obj = page_obj.page(page)
    except PageNotAnInteger:
        page_obj = page_obj.page(1)
    except EmptyPage:
        page_obj = page_obj.page(page_obj.num_pages)
    try:
        filter_parameters = '&client_rfid=' + request.GET['client_rfid']

        filter_parameters += '&client_name=' + request.GET['client_name']
        filter_instance['client_name'] = request.GET['client_name']

        filter_parameters += "&client_surname=" + request.GET['client_surname']
        filter_instance['client_surname'] = request.GET['client_surname']

        filter_parameters += "&date=" + request.GET['date']
        filter_instance['date'] = request.GET['date']
    except:
        filter_parameters = ''
    return render(request, 'clients/attendances.html', {'object_list': object_list, 'page_obj': page_obj, 'filter_parameters': filter_parameters, 'filter_instance': filter_instance})


class trainerAttendanceList(ListView):
    model = trainerAttendanceView


def trainerAttendanceListPages(request):
    qs = trainerAttendanceView.objects.all().order_by('-register_date')
    object_list = TrainersAttendancesFilter(request.GET, queryset=qs).qs
    page_obj = Paginator(object_list, 25)
    page = request.GET.get('page')
    try:
        page_obj = page_obj.page(page)
    except PageNotAnInteger:
        page_obj = page_obj.page(1)
    except EmptyPage:
        page_obj = page_obj.page(page_obj.num_pages)
    filter_instance = {}
    try:
        filter_parameters = '&trainer_rfid=' + request.GET['trainer_rfid']
        filter_instance['trainer_rfid'] = request.GET['trainer_rfid']

        filter_parameters += '&trainer_name=' + request.GET['trainer_name']
        filter_instance['trainer_name'] = request.GET['trainer_name']

        filter_parameters += "&trainer_surname=" + \
            request.GET['trainer_surname']
        filter_instance['trainer_surname'] = request.GET['trainer_surname']

        filter_parameters += "&register_date=" + request.GET['register_date']
        filter_instance['register_date'] = request.GET['register_date']
    except:
        filter_parameters = ''
        filter_instance['register_date'] = ''
        filter_instance['trainer_rfid'] = ''
        filter_instance['trainer_name'] = ''
        filter_instance['trainer_surname'] = ''

    return render(request, 'trainers/attendances.html', {'object_list': object_list, 'page_obj': page_obj, 'filter_parameters': filter_parameters, 'filter_instance': filter_instance})


# ATTENDANCE MODE
class trainersAttendance(ListView):
    model = TRAINERS


def trainersAttendancePages(request):
    qs = TRAINERS.objects.all().order_by('trainer_id')
    object_list = TrainersFilter(request.GET, queryset=qs).qs
    page_obj = Paginator(object_list, 25)
    page = request.GET.get('page')
    try:
        page_obj = page_obj.page(page)
    except PageNotAnInteger:
        page_obj = page_obj.page(1)
    except EmptyPage:
        page_obj = page_obj.page(page_obj.num_pages)
    try:
        filter_parameters = '&trainer_name=' + request.GET['trainer_name']
        filter_parameters += "&trainer_surname=" + \
            request.GET['trainer_surname']
    except:
        filter_parameters = ''
    return render(request, 'trainers/attendanceMode.html', {'object_list': object_list, 'page_obj': page_obj, 'filter_parameters': filter_parameters})


# TRAINERS VIEWS
class TrainerList(ListView):
    model = TRAINERS


def TrainerListPages(request):
    qs = TRAINERS.objects.all().order_by('trainer_id')
    object_list = TrainersFilter(request.GET, queryset=qs).qs
    page_obj = Paginator(object_list, 25)
    page = request.GET.get('page')
    filter_instance = {}
    try:
        page_obj = page_obj.page(page)
    except PageNotAnInteger:
        page_obj = page_obj.page(1)
    except EmptyPage:
        page_obj = page_obj.page(page_obj.num_pages)
    try:
        filter_parameters = '&trainer_name=' + request.GET['trainer_name']
        filter_instance['trainer_name'] = request.GET['trainer_name']
        filter_parameters += "&trainer_surname=" + \
            request.GET['trainer_surname']
        filter_instance['trainer_surname'] = request.GET['trainer_surname']
    except:
        filter_parameters = ''
    return render(request, 'trainers/index.html', {'object_list': object_list, 'page_obj': page_obj, 'filter_parameters': filter_parameters, 'filter_instance': filter_instance})


class TrainerDelete(SuccessMessageMixin, DeleteView):
    model = TRAINERS
    form = TRAINERS
    fields = "__all__"

    def get_success_url(self):
        success_message = '¡Entrenador eliminado correctamente!'
        messages.success(self.request, (success_message))
        return reverse('trainer index')


def TrainerEdit(request, pk):
    trainer = get_object_or_404(TRAINERS, trainer_id=pk)

    if request.method == 'POST':
        requested = request.POST.copy()
        if request.POST.get('change_password', 'off') == 'on':
            requested.pop('change_password')
            form = trainerFormEdit(requested, instance=trainer, initial={'trainer_id': pk})

            if form.is_valid():
                form.save()
                messages.success(request, '¡Entrenador actualizado correctamente!')
                return HttpResponseRedirect(reverse('trainer index'))

        else:
            form = trainerFormEditWithoutPassword(requested, instance=trainer, initial={'trainer_id': pk})

            if form.is_valid():
                form.save()
                messages.success(request, '¡Entrenador actualizado correctamente!')
                return HttpResponseRedirect(reverse('trainer index'))

    elif request.method == 'GET':
        form = trainerFormEdit(request.POST or None, instance=trainer)

    return render(request, 'trainers/edit.html', {'form': form})

# class TrainerEdit(SuccessMessageMixin, UpdateView):
#    model = TRAINERS
#    form_class = trainerForm
#    success_message = '¡Entrenador actualizado correctamente!'
#
#    def get_success_url(self):
#        return reverse('trainer index')


class TrainerDetails(DetailView):
    model = TRAINERS


class TrainerCreate(SuccessMessageMixin, CreateView):
    model = TRAINERS
    form_class = trainerForm
    success_message = '¡Entrenador registrado correctamente!'

    def get_success_url(self):
        return reverse('trainer index')


# CLIENTS VIEWS
class clientsAttendances(ListView):
    model = CLIENTS


def clientsAttendancesPages(request):
    qs = CLIENTS.objects.all().order_by('client_id')
    object_list = ClientsFilter(request.GET, queryset=qs).qs
    page_obj = Paginator(object_list, 25)
    page = request.GET.get('page')
    filter_instance = {}
    try:
        page_obj = page_obj.page(page)
    except PageNotAnInteger:
        page_obj = page_obj.page(1)
    except EmptyPage:
        page_obj = page_obj.page(page_obj.num_pages)
    try:
        filter_parameters = '&client_rfid=' + request.GET['client_rfid']
        filter_parameters += '&client_name=' + request.GET['client_name']
        filter_instance['client_name'] = request.GET['client_name']
        filter_parameters += "&client_surname=" + request.GET['client_surname']
        filter_instance['client_surname'] = request.GET['client_surname']
    except:
        filter_parameters = ''
    return render(request, 'index.html', {'object_list': object_list, 'page_obj': page_obj, 'filter_parameters': filter_parameters, 'filter_instance': filter_instance})


class ClientList(ListView):
    model = CLIENTS


def ClientListPages(request):
    qs = CLIENTS.objects.all().order_by('client_id')
    object_list = ClientsFilter(request.GET, queryset=qs).qs
    page_obj = Paginator(object_list, 25)
    page = request.GET.get('page')
    filter_instance = {}
    try:
        page_obj = page_obj.page(page)
    except PageNotAnInteger:
        page_obj = page_obj.page(1)
    except EmptyPage:
        page_obj = page_obj.page(page_obj.num_pages)
    try:
        filter_parameters = 'client_rfid=' + request.GET['client_rfid']

        filter_parameters += '&client_name=' + request.GET['client_name']
        filter_instance['client_name'] = request.GET['client_name']

        filter_parameters += "&client_surname=" + request.GET['client_surname']
        filter_instance['client_surname'] = request.GET['client_surname']
    except:
        filter_parameters = ''

    return render(request, 'clients/index.html', {'object_list': object_list, 'page_obj': page_obj, 'filter_parameters': filter_parameters, 'filter_instance': filter_instance})


class ClientDetails(DetailView):
    model = CLIENTS


class ClientCreate(SuccessMessageMixin, CreateView):
    model = CLIENTS
    form = CLIENTS
    fields = "__all__"
    success_message = '¡Cliente registrado correctamente!'

    def form_valid(self, form):
        data = form.save()
        membership = MEMBERSHIPS(client_id=CLIENTS(client_id=data.client_id))
        membership.save()
        return redirect('edit membership from create', pk=membership.membership_id)


class ClientEdit(SuccessMessageMixin, UpdateView):
    model = CLIENTS
    form = CLIENTS
    fields = "__all__"
    success_message = '¡Cliente actualizado correctamente!'

    def get_success_url(self):
        return reverse('client index')


class ClientDelete(SuccessMessageMixin, DeleteView):
    model = CLIENTS
    form = CLIENTS
    fields = "__all__"

    def get_success_url(self):
        success_message = '¡Cliente eliminado correctamente!'
        messages.success(self.request, (success_message))
        return reverse('client index')


def Error404(request,  exception):
    return render(request, template_name='errors/404.html')


def Error500(request):
    return render(request, template_name='errors/500.html')


def java_script(request):
    filename = request.path.strip("/")
    print("-"*150)
    print(filename)
    data = open(filename, "rb").read()
    return HttpResponse(data, mimetype="application/x-javascript")
