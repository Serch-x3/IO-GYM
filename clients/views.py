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
    locale.setlocale(locale.LC_ALL, 'es_MX.utf8')
    #General gym stats
    general=[0,0,0,0,0,0]
    general[0]=CLIENTS.objects.count()
    general[1]=TRAINERS.objects.count()
    general[2]=GYMCLASSES.objects.count()
    general[3]=GROUPS.objects.count()
    amc=0
    dmc=0
    memberships=MEMBERSHIPS.objects.all()
    for m in memberships:
        if datetime.now().date() <= m.expiration_date:
            amc=amc+1
        else:
            dmc=dmc+1
    general[4]=amc
    general[5]=dmc

    #Client Flow average per week days last month
    last_month = datetime.now().date() - timedelta(days=30)
    clientAvgPerDayLastMonth=[0,0,0,0,0,0,0] #Index 0 For Sunday
    clientAvgPerDayLastMonth[0]=clientesView.objects.filter(date__week_day=1,date__gte=last_month).count()
    clientAvgPerDayLastMonth[1]=clientesView.objects.filter(date__week_day=2,date__gte=last_month).count()
    clientAvgPerDayLastMonth[2]=clientesView.objects.filter(date__week_day=3,date__gte=last_month).count()
    clientAvgPerDayLastMonth[3]=clientesView.objects.filter(date__week_day=4,date__gte=last_month).count()
    clientAvgPerDayLastMonth[4]=clientesView.objects.filter(date__week_day=5,date__gte=last_month).count()
    clientAvgPerDayLastMonth[5]=clientesView.objects.filter(date__week_day=6,date__gte=last_month).count()
    clientAvgPerDayLastMonth[6]=clientesView.objects.filter(date__week_day=7,date__gte=last_month).count()

    #Client Flow average per week days last 3 months
    last_3month = datetime.now().date() - timedelta(days=90)
    clientAvgPerDayLast3Month=[0,0,0,0,0,0,0] #Index 0 For Sunday
    clientAvgPerDayLast3Month[0]=clientesView.objects.filter(date__week_day=1,date__gte=last_3month).count()/90
    clientAvgPerDayLast3Month[1]=clientesView.objects.filter(date__week_day=2,date__gte=last_3month).count()/90
    clientAvgPerDayLast3Month[2]=clientesView.objects.filter(date__week_day=3,date__gte=last_3month).count()/90
    clientAvgPerDayLast3Month[3]=clientesView.objects.filter(date__week_day=4,date__gte=last_3month).count()/90
    clientAvgPerDayLast3Month[4]=clientesView.objects.filter(date__week_day=5,date__gte=last_3month).count()/90
    clientAvgPerDayLast3Month[5]=clientesView.objects.filter(date__week_day=6,date__gte=last_3month).count()/90
    clientAvgPerDayLast3Month[6]=clientesView.objects.filter(date__week_day=7,date__gte=last_3month).count()/90


    #Client Flow average per week days last 6 months
    last_6month = datetime.now().date() - timedelta(days=183)
    clientAvgPerDayLast6Month=[0,0,0,0,0,0,0] #Index 0 For Sunday
    clientAvgPerDayLast6Month[0]=clientesView.objects.filter(date__week_day=1,date__gte=last_6month).count()/183
    clientAvgPerDayLast6Month[1]=clientesView.objects.filter(date__week_day=2,date__gte=last_6month).count()/183
    clientAvgPerDayLast6Month[2]=clientesView.objects.filter(date__week_day=3,date__gte=last_6month).count()/183
    clientAvgPerDayLast6Month[3]=clientesView.objects.filter(date__week_day=4,date__gte=last_6month).count()/183
    clientAvgPerDayLast6Month[4]=clientesView.objects.filter(date__week_day=5,date__gte=last_6month).count()/183
    clientAvgPerDayLast6Month[5]=clientesView.objects.filter(date__week_day=6,date__gte=last_6month).count()/183
    clientAvgPerDayLast6Month[6]=clientesView.objects.filter(date__week_day=7,date__gte=last_6month).count()/183

    #Client Flow average per week days last year
    last_Year = datetime.now().date() - timedelta(days=365)
    clientAvgPerDayLastYear=[0,0,0,0,0,0,0] #Index 0 For Sunday
    clientAvgPerDayLastYear[0]=clientesView.objects.filter(date__week_day=1,date__gte=last_Year).count()/365
    clientAvgPerDayLastYear[1]=clientesView.objects.filter(date__week_day=2,date__gte=last_Year).count()/365
    clientAvgPerDayLastYear[2]=clientesView.objects.filter(date__week_day=3,date__gte=last_Year).count()/365
    clientAvgPerDayLastYear[3]=clientesView.objects.filter(date__week_day=4,date__gte=last_Year).count()/365
    clientAvgPerDayLastYear[4]=clientesView.objects.filter(date__week_day=5,date__gte=last_Year).count()/365
    clientAvgPerDayLastYear[5]=clientesView.objects.filter(date__week_day=6,date__gte=last_Year).count()/365
    clientAvgPerDayLastYear[6]=clientesView.objects.filter(date__week_day=7,date__gte=last_Year).count()/365


    this_year=datetime.now().date().year
    #Client flow this_year
    clientAvgPerMonthLastYear=[0,0,0,0,0,0,0,0,0,0,0,0] #Index 0 For January
    clientAvgPerMonthLastYear[0]=clientesView.objects.filter(date__month=1,date__year=this_year).count()
    clientAvgPerMonthLastYear[1]=clientesView.objects.filter(date__month=2,date__year=this_year).count()
    clientAvgPerMonthLastYear[2]=clientesView.objects.filter(date__month=3,date__year=this_year).count()
    clientAvgPerMonthLastYear[3]=clientesView.objects.filter(date__month=4,date__year=this_year).count()
    clientAvgPerMonthLastYear[4]=clientesView.objects.filter(date__month=5,date__year=this_year).count()
    clientAvgPerMonthLastYear[5]=clientesView.objects.filter(date__month=6,date__year=this_year).count()
    clientAvgPerMonthLastYear[6]=clientesView.objects.filter(date__month=7,date__year=this_year).count()
    clientAvgPerMonthLastYear[7]=clientesView.objects.filter(date__month=8,date__year=this_year).count()
    clientAvgPerMonthLastYear[8]=clientesView.objects.filter(date__month=9,date__year=this_year).count()
    clientAvgPerMonthLastYear[9]=clientesView.objects.filter(date__month=10,date__year=this_year).count()
    clientAvgPerMonthLastYear[10]=clientesView.objects.filter(date__month=11,date__year=this_year).count()
    clientAvgPerMonthLastYear[11]=clientesView.objects.filter(date__month=12,date__year=this_year).count()


    #New Clients This year
    newClientsPerMonthThisYear=[0,0,0,0,0,0,0,0,0,0,0,0] #Index 0 For January
    newClientsPerMonthThisYear[0]=MEMBERSHIPS.objects.filter(register_date__month=1,register_date__year=this_year).count()
    newClientsPerMonthThisYear[1]=MEMBERSHIPS.objects.filter(register_date__month=2,register_date__year=this_year).count()
    newClientsPerMonthThisYear[2]=MEMBERSHIPS.objects.filter(register_date__month=3,register_date__year=this_year).count()
    newClientsPerMonthThisYear[3]=MEMBERSHIPS.objects.filter(register_date__month=4,register_date__year=this_year).count()
    newClientsPerMonthThisYear[4]=MEMBERSHIPS.objects.filter(register_date__month=5,register_date__year=this_year).count()
    newClientsPerMonthThisYear[5]=MEMBERSHIPS.objects.filter(register_date__month=6,register_date__year=this_year).count()
    newClientsPerMonthThisYear[6]=MEMBERSHIPS.objects.filter(register_date__month=7,register_date__year=this_year).count()
    newClientsPerMonthThisYear[7]=MEMBERSHIPS.objects.filter(register_date__month=8,register_date__year=this_year).count()
    newClientsPerMonthThisYear[8]=MEMBERSHIPS.objects.filter(register_date__month=9,register_date__year=this_year).count()
    newClientsPerMonthThisYear[9]=MEMBERSHIPS.objects.filter(register_date__month=10,register_date__year=this_year).count()
    newClientsPerMonthThisYear[10]=MEMBERSHIPS.objects.filter(register_date__month=11,register_date__year=this_year).count()
    newClientsPerMonthThisYear[11]=MEMBERSHIPS.objects.filter(register_date__month=12,register_date__year=this_year).count()


    #New Clients last year
    startThisMonth=datetime.now().date()- timedelta(days=datetime.now().date().day)
    startThisMonthPrevYear=datetime.now().date()- timedelta(days=datetime.now().date().day+364)
    copy=startThisMonthPrevYear

    monthsLabels=[]
    for x in range(0,12):
        monthsLabels.append(copy.strftime("%B") +" "+ str(copy.year))
        copy=copy+timedelta(days=31)
    yearAgo=MEMBERSHIPS.objects.filter(register_date__year=startThisMonthPrevYear.year,register_date__gte=startThisMonthPrevYear).values_list('register_date__month').annotate(total=Count('client_id')).order_by('register_date__month')
    thisYear=MEMBERSHIPS.objects.filter(register_date__year=startThisMonth.year,register_date__lte=startThisMonth).values_list('register_date__month').annotate(total=Count('client_id')).order_by('register_date__month')

    newClientsPerMonthLastYear=[0,0,0,0,0,0,0,0,0,0,0,0]
    #obtain yearAgo
    f=yearAgo.first()[0] #Number of the first month, It'll works like a index corrector
    for x in yearAgo:
        y=x[0] #Number of month
        newClientsPerMonthLastYear[y-f]=x[1]

    #obtain this year
    f=12-f
    for x in thisYear:
        c=x[0]
        newClientsPerMonthLastYear[c+f]=x[1]


    #Client Flow Last year
    yearAgoF=clientesView.objects.filter(date__year=startThisMonthPrevYear.year,date__gte=startThisMonthPrevYear).values_list('date__month').annotate(total=Count('id')).order_by('date__month')
    thisYearF=clientesView.objects.filter(date__year=startThisMonth.year,date__lte=startThisMonth).values_list('date__month').annotate(total=Count('id')).order_by('date__month')

    ClientsPerMonthLastYear=[0,0,0,0,0,0,0,0,0,0,0,0]
    #obtain yearAgo
    ff=yearAgo.first()[0] #Number of the first month, It'll works like a index corrector

    for x in yearAgoF:
        y=x[0] #Number of month
        ClientsPerMonthLastYear[y-ff]=x[1]

    #obtain this year
    ff=12-ff
    for x in thisYearF:
        c=x[0]
        ClientsPerMonthLastYear[c+ff]=x[1]
    print(ClientsPerMonthLastYear)
    return render(request,'admin/graphs/index.html',{
        'general': general,
        'clientAvgPerDayLastMonth':clientAvgPerDayLastMonth,
        'clientAvgPerDayLast3Month':clientAvgPerDayLast3Month,
        'clientAvgPerDayLast6Month':clientAvgPerDayLast6Month,
        'clientAvgPerDayLastYear':clientAvgPerDayLastYear,
        'clientAvgPerMonthLastYear':clientAvgPerMonthLastYear,
        'newClientsPerMonthThisYear':newClientsPerMonthThisYear,
        'newClientsPerMonthLastYear':newClientsPerMonthLastYear,
        'monthsLabels':monthsLabels,
        'startThisMonth':startThisMonth,
        'startThisMonthPrevYear':startThisMonthPrevYear,
        'ClientsPerMonthLastYear':ClientsPerMonthLastYear,
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
    success_message = '¡Hora creada correctamente!' # Mostramos este Mensaje luego de Crear un Postre

    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):
        return reverse('index hours') # Redireccionamos a la vista principal 'leer'

class hoursDelete(SuccessMessageMixin, DeleteView):
    model = HOURS
    form = HOURS
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = '¡Hora eliminada correctamente!' # Mostramos este Mensaje luego de Editar un Postre
        messages.success (self.request, (success_message))
        return reverse('index hours') # Redireccionamos a la vista principal 'leer'

class hoursView(ListView):
    model= HOURS

class weekdaysCreate(SuccessMessageMixin, CreateView):
    model = WEEKDAYS
    form = WEEKDAYS
    fields = "__all__"
    success_message = '¡Día creado correctamente!' # Mostramos este Mensaje luego de Crear un Postre

    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):
        return reverse('index weekdays') # Redireccionamos a la vista principal 'leer'

class weekdayDelete(SuccessMessageMixin, DeleteView):
    model = WEEKDAYS
    form = WEEKDAYS
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = '¡Día eliminado correctamente!' # Mostramos este Mensaje luego de Editar un Postre
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
