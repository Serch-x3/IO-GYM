from django.core.validators import MaxValueValidator
from django.core.validators import MinLengthValidator
from django.core.validators import MinValueValidator
from django.core.validators import EmailValidator
from django.db import models
from model_utils import Choices
import time
from datetime import datetime, timedelta
from django.shortcuts import get_list_or_404, get_object_or_404
from fernet_fields import fields
# Create your models here.

class GeneralStats(models.Model):
    id = models.IntegerField(verbose_name='id', db_column='id'),
    clients = models.IntegerField(verbose_name='Clientes', db_column='clients');
    trainers = models.IntegerField(verbose_name='Entrenadores', db_column='trainers');
    groups = models.IntegerField(verbose_name='Grupos', db_column='groups');
    classes = models.IntegerField(verbose_name='Clases', db_column='classes');
    active_memberships = models.IntegerField(verbose_name='Membresías Activas', db_column='active_memberships');
    expirated_memberships = models.IntegerField(verbose_name='Membresías Expiradas.', db_column='expirated_memberships');

    class Meta:
        managed = False
        db_table = 'GeneralStats'

class CFLM(models.Model):
    id = models.IntegerField(db_column='id'),
    monday = models.IntegerField(db_column='monday');
    tuesday = models.IntegerField(db_column='tuesday');
    wednesday = models.IntegerField(db_column='wednesday');
    thursday = models.IntegerField(db_column='thursday');
    friday = models.IntegerField(db_column='friday');
    saturday = models.IntegerField(db_column='saturday');
    sunday = models.IntegerField(db_column='sunday');

    class Meta:
        managed = False
        db_table = 'CFLM'

class CFL3M(models.Model):
    id = models.IntegerField(db_column='id'),
    monday = models.IntegerField(db_column='monday');
    tuesday = models.IntegerField(db_column='tuesday');
    wednesday = models.IntegerField(db_column='wednesday');
    thursday = models.IntegerField(db_column='thursday');
    friday = models.IntegerField(db_column='friday');
    saturday = models.IntegerField(db_column='saturday');
    sunday = models.IntegerField(db_column='sunday');

    class Meta:
        managed = False
        db_table = 'CFL3M'

class CFL6M(models.Model):
    id = models.IntegerField(db_column='id'),
    monday = models.IntegerField(db_column='monday');
    tuesday = models.IntegerField(db_column='tuesday');
    wednesday = models.IntegerField(db_column='wednesday');
    thursday = models.IntegerField(db_column='thursday');
    friday = models.IntegerField(db_column='friday');
    saturday = models.IntegerField(db_column='saturday');
    sunday = models.IntegerField(db_column='sunday');

    class Meta:
        managed = False
        db_table = 'CFL6M'

class CFLY(models.Model):
    id = models.IntegerField(db_column='id'),
    monday = models.IntegerField(db_column='monday');
    tuesday = models.IntegerField(db_column='tuesday');
    wednesday = models.IntegerField(db_column='wednesday');
    thursday = models.IntegerField(db_column='thursday');
    friday = models.IntegerField(db_column='friday');
    saturday = models.IntegerField(db_column='saturday');
    sunday = models.IntegerField(db_column='sunday');

    class Meta:
        managed = False
        db_table = 'CFLY'

class HCLYD(models.Model):
    id = models.IntegerField(db_column='id'),
    monday = models.IntegerField(db_column='monday');
    tuesday = models.IntegerField(db_column='tuesday');
    wednesday = models.IntegerField(db_column='wednesday');
    thursday = models.IntegerField(db_column='thursday');
    friday = models.IntegerField(db_column='friday');
    saturday = models.IntegerField(db_column='saturday');
    sunday = models.IntegerField(db_column='sunday');

    class Meta:
        managed = False
        db_table = 'HCLYD'

class CFLYM(models.Model):
    id = models.IntegerField(db_column='id'),
    records = models.IntegerField(db_column='records');
    month_number = models.IntegerField(db_column='month_number');
    year = models.IntegerField(db_column='year');

    class Meta:
        managed = False
        db_table = 'CFLYM'

class HCFM(models.Model):
    id = models.IntegerField(db_column='id'),
    records = models.IntegerField(db_column='records');
    month_number = models.IntegerField(db_column='month_number');
    year = models.IntegerField(db_column='year');

    class Meta:
        managed = False
        db_table = 'HCFM'

class NCLYM(models.Model):
    id = models.IntegerField(db_column='id'),
    records = models.IntegerField(db_column='records');
    month_number = models.IntegerField(db_column='month_number');
    year = models.IntegerField(db_column='year');

    class Meta:
        managed = False
        db_table = 'NCLYM'

class trainerAttendanceView(models.Model):
    id=models.CharField(primary_key=True),
    trainer_name=models.CharField(verbose_name='Nombre', db_column='trainer_name',max_length=40);
    trainer_surname=models.CharField(verbose_name='Apellidos', db_column='trainer_surname',max_length=40);
    register_date=models.DateField(verbose_name='Fecha', db_column='register_date');
    description=models.CharField(verbose_name='Descripción', db_column='description',max_length=40);

    class Meta:
        managed = False
        db_table = 'trainerAttendanceView'

class clientAttendanceView(models.Model):
    id = models.BigIntegerField(primary_key=True),
    client_name=models.CharField(max_length=40, verbose_name='Nombre')
    client_surname=models.CharField(max_length=40, verbose_name='Apellidos')
    date=models.DateField(verbose_name='Fecha')

    class Meta:
        managed = False
        db_table = 'clientAttendanceView'

class MEMBERSHIPS(models.Model):
    def get_cancel():
        return (datetime.now() - timedelta(days=1)).date()
    def get_today():
        return datetime.now().date()
    def get_weeks(number):
        return (datetime.now() + timedelta(weeks=number)).date()
    def get_months(number):
        return (datetime.now() + timedelta(days=number*30)).date()
    def get_years(number):
        return (datetime.now() + timedelta(days=number*365)).date()
    cancel=get_cancel()
    today=get_today()
    oneWeek=get_weeks(1)
    oneMonth=get_months(1)
    threeMonth=get_months(3)
    sixMonth=get_months(6)
    oneYear=get_years(1)
    DATE_SELECTION = Choices(
            (cancel, "Cancelado"),
            (today, "Visita (solo hoy)"),
            (oneWeek, "1 semana"),
            (oneMonth, "1 mes"),
            (threeMonth, "3 meses"),
            (sixMonth, "6 meses"),
            (oneYear, "1 año"),
        )
    membership_id = models.AutoField(primary_key=True)
    client_id = models.OneToOneField('CLIENTS', on_delete=models.CASCADE, db_column='client_id', blank=True, verbose_name='Cliente')
    included_classes= models.ManyToManyField('GYMCLASSES', verbose_name='Clases incluidas')
    register_date = models.DateField(auto_now_add=True, verbose_name='Fecha de registro')
    expiration_date = models.DateField(choices=DATE_SELECTION, default=today, verbose_name='Duración', null=False, blank=False)

    class Meta:
        managed = True
        db_table = 'MEMBERSHIPS'



class CLIENTS_ATTENDANCES(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey('CLIENTS', models.DO_NOTHING, db_column='client_id', blank=True, null=False, verbose_name='Cliente')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')

    class Meta:
        managed = True
        db_table = 'CLIENT_ATTENDANCES'


class TRAINERS_ATTENDANCES(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    trainer_id = models.ForeignKey('TRAINERS', models.DO_NOTHING, db_column='trainer_id', blank=True, verbose_name='Entrenador')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    description = models.CharField(max_length=10, blank=True, null=False, verbose_name='Fecha')

    class Meta:
        managed = True
        db_table = 'TRAINNERS_ATTENDANCES'

class CLIENTS(models.Model):
    emailValidator= EmailValidator(message="Email inválido")
    options=Choices(('M','Masculino'),('F','Femenino'),('N','No binario'))
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=40, blank=True, null=False, verbose_name='Nombre')
    client_surname = models.CharField(max_length=40, blank=True, null=True, verbose_name='Apellidos')
    client_birthday = models.DateField(verbose_name='Fecha de nacimiento')
    client_phone = models.CharField(max_length=12,blank=True, null=True, verbose_name='Teléfono')
    client_emergency_phone = models.CharField(max_length=12,blank=True, verbose_name='Teléfono de emergencias')
    client_email = models.CharField(max_length=40, blank=True, null=True, validators=[emailValidator], verbose_name='Email')
    client_gender = models.CharField(choices=options,max_length=1, blank=True, null=True, verbose_name='Género')
    client_medical_info = models.CharField(max_length=200, null=True, blank=True, verbose_name='Información Médica')
    client_rfid = models.CharField(max_length=10, blank=True, null=True, unique=True, verbose_name='Llave de acceso')

    class Meta:
        managed = True
        db_table = 'CLIENTS'

    def __str__(self):
        return self.client_name+' '+self.client_surname


class GYMCLASSES(models.Model):
    gymclass_id = models.AutoField(primary_key=True)
    gymclass_name = models.CharField(max_length=40, blank=True, verbose_name='Nombre')

    class Meta:
        managed = True
        db_table = 'GYMCLASSES'

    def __str__(self):
        return self.gymclass_name



class TRAINERS(models.Model):
    emailValidator= EmailValidator(message="Email inválido")
    options=Choices(('M','Masculino'),('F','Femenino'),('N','No binario'))
    trainer_id = models.AutoField(primary_key=True)
    trainer_name = models.CharField(max_length=40, blank=True, verbose_name='Nombre')
    trainer_surname = models.CharField(max_length=40, blank=True, null=True, verbose_name='Apellidos')
    trainer_birthday = models.DateField(verbose_name='Fecha de nacimiento')
    trainer_phone = models.CharField(max_length=12,blank=True, null=True, verbose_name='Teléfono')
    trainer_emergency_phone = models.CharField(max_length=12,blank=True, verbose_name='Teléfono de emergencia')
    trainer_email = models.CharField(max_length=40, blank=True, null=True, validators=[emailValidator], verbose_name='Email')
    trainer_gender = models.CharField(choices=options, max_length=1, blank=True, null=True, verbose_name='Género')
    trainer_address = models.CharField(max_length=60, blank=True, null=True, verbose_name='Dirección')
    trainer_rfc = models.CharField(validators=[MinLengthValidator(12)], max_length=13, blank=True, null=True, verbose_name='RFC')
    trainer_password = fields.EncryptedTextField(max_length=40, blank=True, verbose_name='Contraseña')
    trainer_rfid = models.CharField(max_length=10, blank=True, null=True, unique=True, verbose_name='Llave de acceso')

    class Meta:
        managed = True
        db_table = 'TRAINNERS'

    def __str__(self):
        return self.trainer_name+' '+self.trainer_surname


class GROUPS(models.Model):
    options=Choices('Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo')
    group_id = models.AutoField(primary_key=True)
    gymclass_id = models.ForeignKey('GYMCLASSES', models.DO_NOTHING, db_column='gymclass_id', blank=True, null=True, verbose_name='Clase')
    trainer_id = models.ForeignKey('TRAINERS', models.DO_NOTHING, db_column='trainer_id', blank=True, null=True, verbose_name='Entrenador')
    weekday = models.CharField(choices=options, max_length=15, verbose_name='Día', blank=False, null=False )
    hour = models.CharField(max_length=10, null=True, verbose_name='Hora')
    class Meta:
        managed = True
        db_table = 'GROUPS'
