from django.contrib.auth.models import *
import django_filters
from .models import *

class ClientsFilter(django_filters.FilterSet):
    client_name=django_filters.CharFilter(lookup_expr='icontains', label="Nombre")
    client_surname=django_filters.CharFilter(lookup_expr='icontains', label="Apellidos")
    class Meta:
        model = CLIENTS
        fields = ['client_name', 'client_surname', ]

class TrainersFilter(django_filters.FilterSet):
    trainer_name=django_filters.CharFilter(lookup_expr='icontains', label="Nombre")
    trainer_surname=django_filters.CharFilter(lookup_expr='icontains', label="Apellidos")
    class Meta:
        model = TRAINERS
        fields = ['trainer_name', 'trainer_surname', ]
