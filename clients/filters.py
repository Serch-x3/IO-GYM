from django.contrib.auth.models import *
import django_filters
from .models import *

class ClientsFilter(django_filters.FilterSet):
    client_name=django_filters.CharFilter(lookup_expr='icontains', label="Nombre")
    client_surname=django_filters.CharFilter(lookup_expr='icontains', label="Apellidos")
    class Meta:
        model = CLIENTS
        fields = ['client_name', 'client_surname', ]

class ClientsFilterForAttendance(django_filters.FilterSet):
    client_name=django_filters.CharFilter(lookup_expr='icontains', label="Nombre")
    client_surname=django_filters.CharFilter(lookup_expr='icontains', label="Apellidos")
    class Meta:
        model = CLIENTS
        fields = ['client_name', 'client_surname', ]

class ClientsAttendancesFilter(django_filters.FilterSet):
    id=django_filters.CharFilter(lookup_expr='icontains', label="Nombre")
    date=django_filters.DateRangeFilter(field_name='date')

    class Meta:
        model = clientesView
        fields = ['id', 'date', ]



class TrainersFilter(django_filters.FilterSet):
    trainer_name=django_filters.CharFilter(lookup_expr='icontains', label="Nombre")
    trainer_surname=django_filters.CharFilter(lookup_expr='icontains', label="Apellidos")
    class Meta:
        model = TRAINERS
        fields = ['trainer_name', 'trainer_surname', ]


class TrainersAttendancesFilter(django_filters.FilterSet):
    id=django_filters.CharFilter(lookup_expr='icontains', label="Nombre")
    trainer_surname=django_filters.CharFilter(lookup_expr='icontains', label="Apellidos")
    date=django_filters.DateRangeFilter(field_name='register_date')

    class Meta:
        model = trainerAttendanceView
        fields = ['id', 'trainer_surname','register_date', ]
