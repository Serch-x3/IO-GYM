from django.core.validators import MaxValueValidator
from django.core.validators import MinLengthValidator
from django.core.validators import MinValueValidator
from django.core.validators import EmailValidator
from django.db import models
from model_utils import Choices
import time
from datetime import datetime, timedelta
from django.shortcuts import get_list_or_404, get_object_or_404
# Create your models here.

class trainerAttendanceView(models.Model):
    id=models.CharField(verbose_name='Nombre'),
    trainer_surname=models.CharField(verbose_name='Apellidos', db_column='trainer_surname',max_length=40);
    trainer_phone=models.CharField(verbose_name='Teléfono', db_column='trainer_phone',max_length=40);
    register_date=models.DateField(verbose_name='Fecha', db_column='register_date',max_length=40);
    description=models.CharField(verbose_name='Descripción', db_column='description',max_length=40);

    class Meta:
        managed = False
        db_table = 'trainerAttendanceView'

class clientesView(models.Model):
    id=models.CharField(verbose_name='Cliente'),
    date=models.DateField(verbose_name='Fecha');

    class Meta:
        managed = False
        db_table = 'clientesView'

class MEMBERSHIPS(models.Model):
    def get_today():
        return datetime.now().date()
    def get_weeks(number):
        return (datetime.now() + timedelta(weeks=number)).date()
    def get_months(number):
        return (datetime.now() + timedelta(days=number*30)).date()
    def get_years(number):
        return (datetime.now() + timedelta(days=number*365)).date()
    today=get_today()
    oneWeek=get_weeks(1)
    oneMonth=get_months(1)
    threeMonth=get_months(3)
    sixMonth=get_months(6)
    oneYear=get_years(1)
    DATE_SELECTION = Choices(
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
    expiration_date = models.DateField(choices=DATE_SELECTION,verbose_name='Duración', null=True, blank=True)

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
    client_phone = models.BigIntegerField(validators=[MinValueValidator(1000000,message="El Numero debe ser de al menos 7 dígitos y no negativo"),MaxValueValidator(9999999999,message="El Numero debe ser de máximo 10 dígitos")],blank=True, null=True, verbose_name='Teléfono')
    client_emergency_phone = models.BigIntegerField(validators=[MinValueValidator(1000000,message="El Numero debe ser de al menos 7 dígitos y no negativo"),MaxValueValidator(9999999999,message="El Numero debe ser de máximo 10 dígitos")],blank=True, verbose_name='Teléfono de emergencias')
    client_email = models.CharField(max_length=40, blank=True, null=True, validators=[emailValidator], verbose_name='Email')
    client_gender = models.CharField(choices=options,max_length=1, blank=True, null=True, verbose_name='Género')

    class Meta:
        managed = True
        db_table = 'CLIENTS'

    def __str__(self):
        return self.client_name+' '+self.client_surname

    def delete(self, *args, **kwargs):
        CLIENTS_ATTENDANCES.objects.filter(client_id=self.client_id).delete()
        MEMBERSHIPS.objects.filter(client_id=self.client_id).delete()
        super(CLIENTS, self).delete(*args, **kwargs)


class GYMCLASSES(models.Model):
    gymclass_id = models.AutoField(primary_key=True)
    gymclass_name = models.CharField(max_length=40, blank=True, verbose_name='Nombre')
    class Meta:
        managed = True
        db_table = 'GYMCLASSES'
    def __str__(self):
        return self.gymclass_name

    def delete(self, *args, **kwargs):
        for m in MEMBERSHIPS.objects.all():
            m.included_classes.remove(self)
        GROUPS.objects.filter(gymclass_id=self.gymclass_id).update(gymclass_id=None)
        super(GYMCLASSES, self).delete(*args, **kwargs)

class TRAINERS(models.Model):
    emailValidator= EmailValidator(message="Email inválido")
    options=Choices(('M','Masculino'),('F','Femenino'),('N','No binario'))
    trainer_id = models.AutoField(primary_key=True)
    trainer_name = models.CharField(max_length=40, blank=True, verbose_name='Nombre')
    trainer_surname = models.CharField(max_length=40, blank=True, null=True, verbose_name='Apellidos')
    trainer_birthday = models.DateField(verbose_name='Fecha de nacimiento')
    trainer_phone = models.BigIntegerField(validators=[MinValueValidator(1000000,message="El Numero debe ser de al menos 7 dígitos y no negativo"),MaxValueValidator(9999999999,message="El Numero debe ser de máximo 10 dígitos")],blank=True, null=True, verbose_name='Teléfono')
    trainer_emergency_phone = models.BigIntegerField(validators=[MinValueValidator(1000000,message="El Numero debe ser de al menos 7 dígitos y no negativo"),MaxValueValidator(9999999999,message="El Numero debe ser de máximo 10 dígitos")],blank=True, verbose_name='Teléfono de emergencia')
    trainer_email = models.CharField(max_length=40, blank=True, null=True, validators=[emailValidator], verbose_name='Email')
    trainer_gender = models.CharField(choices=options, max_length=1, blank=True, null=True, verbose_name='Género')
    trainer_address = models.CharField(max_length=60, blank=True, null=True, verbose_name='Dirección')
    trainer_rfc = models.CharField(validators=[MinLengthValidator(12)], max_length=13, blank=True, null=True, verbose_name='RFC')
    trainer_password = models.CharField(max_length=40, blank=True, verbose_name='Contraseña')

    class Meta:
        managed = True
        db_table = 'TRAINNERS'

    def __str__(self):
        return self.trainer_name+' '+self.trainer_surname

    def delete(self, *args, **kwargs):
        GROUPS.objects.filter(trainer_id=self.trainer_id).update(trainer_id=None)
        TRAINERS_ATTENDANCES.objects.filter(trainer_id=self.trainer_id).delete()
        super(TRAINERS, self).delete(*args, **kwargs)

class WEEKDAYS(models.Model):
    options=Choices('Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo')
    weekdays_id = models.AutoField(primary_key=True)
    weekdays_name = models.CharField(unique=True, choices=options,max_length=15, verbose_name='Día')

    class Meta:
        managed = True
        db_table = 'WEEKDAYS'

    def __str__(self):
        return self.weekdays_name

    def delete(self, *args, **kwargs):
        GROUPS.objects.filter(weekday_id=self.weekdays_id).update(weekday_id=None)
        super(WEEKDAYS, self).delete(*args, **kwargs)

class HOURS(models.Model):
    hour_id = models.AutoField(primary_key=True)
    hour_name = models.CharField(max_length=20, verbose_name='Hora')

    class Meta:
        managed = True
        db_table = 'HOURS'
    def __str__(self):
        return self.hour_name

    def delete(self, *args, **kwargs):
        GROUPS.objects.filter(hour_id=self.hour_id).update(hour_id=None)
        super(HOURS, self).delete(*args, **kwargs)


class GROUPS(models.Model):
    group_id = models.AutoField(primary_key=True)
    gymclass_id = models.ForeignKey('GYMCLASSES', models.DO_NOTHING, db_column='gymclass_id', blank=True, null=True, verbose_name='Clase')
    trainer_id = models.ForeignKey('TRAINERS', models.DO_NOTHING, db_column='trainer_id', blank=True, null=True, verbose_name='Entrenador')
    weekday_id = models.ForeignKey('WEEKDAYS', models.DO_NOTHING, db_column='weekdays_id', blank=True, null=True, verbose_name='Día')
    hour_id = models.ForeignKey('HOURS', models.DO_NOTHING, db_column='hour_id', blank=True, null=True, verbose_name='Hora')
    class Meta:
        managed = True
        db_table = 'GROUPS'
