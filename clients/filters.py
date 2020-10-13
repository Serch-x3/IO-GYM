from django.contrib.auth.models import *
import django_filters as filters
from .models import *

class ClientsFilter(filters.FilterSet):
    client_name=filters.CharFilter(lookup_expr='icontains', label="Nombre")
    client_surname=filters.CharFilter(lookup_expr='icontains', label="Apellidos")
    client_rfid=filters.CharFilter(lookup_expr='iexact', label="Llave de acceso")

    class Meta:
        model = CLIENTS
        fields = ['client_name', 'client_surname', 'client_rfid']


class TrainersAttendancesFilter(filters.FilterSet):
    trainer_name=filters.CharFilter(lookup_expr='icontains', label="Nombre")
    trainer_surname=filters.CharFilter(lookup_expr='icontains', label="Apellidos")
    trainer_rfid=filters.CharFilter(lookup_expr='iexact', label="Llave de acceso")
    register_date=filters.DateRangeFilter()

    class Meta:
        model = trainerAttendanceView
        fields = ['trainer_name','trainer_surname','register_date']


class ClientsAttendancesFilter(filters.FilterSet):
    client_name=filters.CharFilter(lookup_expr='icontains', label="Nombre")
    client_surname=filters.CharFilter(lookup_expr='icontains', label="Apellidos")
    client_rfid=filters.CharFilter(lookup_expr='iexact', label="Llave de acceso")
    date=filters.DateRangeFilter(field_name='date')

    class Meta:
        model = clientAttendanceView
        fields = ['client_name', 'client_surname', 'date', ]



class TrainersFilter(filters.FilterSet):
    trainer_name=filters.CharFilter(lookup_expr='icontains', label="Nombre")
    trainer_surname=filters.CharFilter(lookup_expr='icontains', label="Apellidos")
    trainer_rfid=filters.CharFilter(lookup_expr='iexact', label="Llave de acceso")

    class Meta:
        model = TRAINERS
        paginate_by = 1
        fields = ['trainer_name', 'trainer_surname', 'trainer_rfid',]
