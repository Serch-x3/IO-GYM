# Generated by Django 3.1.3 on 2020-12-02 11:58

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import fernet_fields.fields
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CFL3M',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', models.IntegerField(db_column='monday')),
                ('tuesday', models.IntegerField(db_column='tuesday')),
                ('wednesday', models.IntegerField(db_column='wednesday')),
                ('thursday', models.IntegerField(db_column='thursday')),
                ('friday', models.IntegerField(db_column='friday')),
                ('saturday', models.IntegerField(db_column='saturday')),
                ('sunday', models.IntegerField(db_column='sunday')),
            ],
            options={
                'db_table': 'CFL3M',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CFL6M',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', models.IntegerField(db_column='monday')),
                ('tuesday', models.IntegerField(db_column='tuesday')),
                ('wednesday', models.IntegerField(db_column='wednesday')),
                ('thursday', models.IntegerField(db_column='thursday')),
                ('friday', models.IntegerField(db_column='friday')),
                ('saturday', models.IntegerField(db_column='saturday')),
                ('sunday', models.IntegerField(db_column='sunday')),
            ],
            options={
                'db_table': 'CFL6M',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CFLM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', models.IntegerField(db_column='monday')),
                ('tuesday', models.IntegerField(db_column='tuesday')),
                ('wednesday', models.IntegerField(db_column='wednesday')),
                ('thursday', models.IntegerField(db_column='thursday')),
                ('friday', models.IntegerField(db_column='friday')),
                ('saturday', models.IntegerField(db_column='saturday')),
                ('sunday', models.IntegerField(db_column='sunday')),
            ],
            options={
                'db_table': 'CFLM',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CFLY',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', models.IntegerField(db_column='monday')),
                ('tuesday', models.IntegerField(db_column='tuesday')),
                ('wednesday', models.IntegerField(db_column='wednesday')),
                ('thursday', models.IntegerField(db_column='thursday')),
                ('friday', models.IntegerField(db_column='friday')),
                ('saturday', models.IntegerField(db_column='saturday')),
                ('sunday', models.IntegerField(db_column='sunday')),
            ],
            options={
                'db_table': 'CFLY',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CFLYM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('records', models.IntegerField(db_column='records')),
                ('month_number', models.IntegerField(db_column='month_number')),
                ('year', models.IntegerField(db_column='year')),
            ],
            options={
                'db_table': 'CFLYM',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='clientAttendanceView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=40, verbose_name='Nombre')),
                ('client_surname', models.CharField(max_length=40, verbose_name='Apellidos')),
                ('client_rfid', models.CharField(blank=True, max_length=10, null=True, unique=True, verbose_name='Llave de acceso')),
                ('date', models.DateField(verbose_name='Fecha')),
            ],
            options={
                'db_table': 'clientAttendanceView',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GeneralStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clients', models.IntegerField(db_column='clients', verbose_name='Clientes')),
                ('trainers', models.IntegerField(db_column='trainers', verbose_name='Entrenadores')),
                ('groups', models.IntegerField(db_column='groups', verbose_name='Grupos')),
                ('classes', models.IntegerField(db_column='classes', verbose_name='Clases')),
                ('active_memberships', models.IntegerField(db_column='active_memberships', verbose_name='Membresías Activas')),
                ('expirated_memberships', models.IntegerField(db_column='expirated_memberships', verbose_name='Membresías Expiradas.')),
            ],
            options={
                'db_table': 'GeneralStats',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HCFM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('records', models.IntegerField(db_column='records')),
                ('month_number', models.IntegerField(db_column='month_number')),
                ('year', models.IntegerField(db_column='year')),
            ],
            options={
                'db_table': 'HCFM',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HCLYD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', models.IntegerField(db_column='monday')),
                ('tuesday', models.IntegerField(db_column='tuesday')),
                ('wednesday', models.IntegerField(db_column='wednesday')),
                ('thursday', models.IntegerField(db_column='thursday')),
                ('friday', models.IntegerField(db_column='friday')),
                ('saturday', models.IntegerField(db_column='saturday')),
                ('sunday', models.IntegerField(db_column='sunday')),
            ],
            options={
                'db_table': 'HCLYD',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IBM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_income', models.DecimalField(db_column='month_income', decimal_places=2, max_digits=19, verbose_name='Ingreso mensual')),
                ('month', models.CharField(db_column='month', max_length=30, verbose_name='Mes')),
                ('year', models.CharField(db_column='year', max_length=30, verbose_name='Año')),
            ],
            options={
                'db_table': 'IBM',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MSM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sales', models.IntegerField(db_column='sales', verbose_name='Membresías vendidas')),
                ('month', models.CharField(db_column='month', max_length=30, verbose_name='Mes')),
                ('year', models.CharField(db_column='year', max_length=30, verbose_name='Año')),
            ],
            options={
                'db_table': 'MSM',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NCLYM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('records', models.IntegerField(db_column='records')),
                ('month_number', models.IntegerField(db_column='month_number')),
                ('year', models.IntegerField(db_column='year')),
            ],
            options={
                'db_table': 'NCLYM',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='trainerAttendanceView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainer_name', models.CharField(db_column='trainer_name', max_length=40, verbose_name='Nombre')),
                ('trainer_surname', models.CharField(db_column='trainer_surname', max_length=40, verbose_name='Apellidos')),
                ('trainer_rfid', models.CharField(blank=True, max_length=10, null=True, unique=True, verbose_name='Llave de acceso')),
                ('register_date', models.DateField(db_column='register_date', verbose_name='Fecha')),
                ('description', models.CharField(db_column='description', max_length=40, verbose_name='Descripción')),
            ],
            options={
                'db_table': 'trainerAttendanceView',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CLIENTS',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=40, validators=[django.core.validators.RegexValidator('^[a-zA-ZÁáÉéÍíÓóÚú]*$', 'Sólo se permiten letras')], verbose_name='Nombre')),
                ('client_surname', models.CharField(max_length=40, validators=[django.core.validators.RegexValidator('^[a-zA-ZÁáÉéÍíÓóÚú]*$', 'Sólo se permiten letras')], verbose_name='Apellidos')),
                ('client_birthday', models.DateField(verbose_name='Fecha de nacimiento')),
                ('client_phone', models.CharField(max_length=12, verbose_name='Teléfono')),
                ('client_emergency_phone', models.CharField(max_length=12, verbose_name='Teléfono de emergencias')),
                ('client_email', models.CharField(blank=True, max_length=40, null=True, validators=[django.core.validators.EmailValidator(message='Email inválido')], verbose_name='Email')),
                ('client_gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('N', 'No binario')], max_length=1, verbose_name='Género')),
                ('client_medical_info', models.CharField(default='Sin padecimientos', max_length=200, verbose_name='Información Médica')),
                ('client_rfid', models.CharField(blank=True, max_length=10, null=True, unique=True, verbose_name='Llave de acceso')),
            ],
            options={
                'verbose_name': 'Cliente',
                'db_table': 'CLIENTS',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GYMCLASSES',
            fields=[
                ('gymclass_id', models.AutoField(primary_key=True, serialize=False)),
                ('gymclass_name', models.CharField(max_length=40, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid')], verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'clase',
                'db_table': 'GYMCLASSES',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PAYMENTS',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.PositiveIntegerField(blank=True, default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Cantidad')),
                ('time_type', models.CharField(choices=[('Día', 'Día'), ('Semana', 'Semana'), ('Mes', 'Mes'), ('Año', 'Año')], default='Días', max_length=15, verbose_name='Unidad de tiempo')),
                ('payment_description', models.CharField(max_length=40, unique=True, verbose_name='Descripcion')),
                ('payment_cost', models.FloatField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Costo')),
            ],
            options={
                'verbose_name': 'pago',
                'db_table': 'PAYMENTS',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TRAINERS',
            fields=[
                ('trainer_id', models.AutoField(primary_key=True, serialize=False)),
                ('trainer_name', models.CharField(max_length=40, validators=[django.core.validators.RegexValidator('^[a-zA-ZÁáÉéÍíÓóÚú]*$', 'Sólo se permiten letras')], verbose_name='Nombre')),
                ('trainer_surname', models.CharField(max_length=40, validators=[django.core.validators.RegexValidator('^[a-zA-ZÁáÉéÍíÓóÚú]*$', 'Sólo se permiten letras')], verbose_name='Apellidos')),
                ('trainer_birthday', models.DateField(verbose_name='Fecha de nacimiento')),
                ('trainer_phone', models.CharField(max_length=12, verbose_name='Teléfono')),
                ('trainer_emergency_phone', models.CharField(max_length=12, verbose_name='Teléfono de emergencia')),
                ('trainer_email', models.CharField(blank=True, max_length=40, null=True, validators=[django.core.validators.EmailValidator(message='Email inválido')], verbose_name='Email')),
                ('trainer_gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('N', 'No binario')], max_length=1, verbose_name='Género')),
                ('trainer_address', models.CharField(blank=True, max_length=60, null=True, verbose_name='Dirección')),
                ('trainer_rfc', models.CharField(blank=True, max_length=13, null=True, validators=[django.core.validators.MinLengthValidator(12), django.core.validators.RegexValidator('^[0-9a-zA-ZÁáÉéÍíÓóÚú]*$', 'Sólo se permiten carácteres alfanuméricos (0-9 y A-Z).')], verbose_name='RFC')),
                ('trainer_password', fernet_fields.fields.EncryptedTextField(max_length=40, verbose_name='Contraseña')),
                ('trainer_rfid', models.CharField(blank=True, default=None, max_length=10, null=True, unique=True, verbose_name='Llave de acceso')),
            ],
            options={
                'verbose_name': 'Entrenador',
                'db_table': 'TRAINNERS',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TRAINERS_ATTENDANCES',
            fields=[
                ('attendance_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('description', models.CharField(blank=True, max_length=10, verbose_name='Fecha')),
                ('trainer_id', models.ForeignKey(blank=True, db_column='trainer_id', on_delete=django.db.models.deletion.DO_NOTHING, to='clients.trainers', verbose_name='Entrenador')),
            ],
            options={
                'db_table': 'TRAINNERS_ATTENDANCES',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PAYMENTS_REGISTERS',
            fields=[
                ('payment_register_id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_concept', models.CharField(default='Sin especificar', max_length=40, verbose_name='Concepto')),
                ('payment_cost', models.FloatField(blank=True, default='1', verbose_name='Costo')),
                ('payment_date', models.DateField(auto_now_add=True, null=True, verbose_name='Fecha de registro')),
                ('client_id', models.ForeignKey(db_column='client_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='clients.clients')),
            ],
            options={
                'db_table': 'PAYMENTS_REGISTERS',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MEMBERSHIPS',
            fields=[
                ('membership_id', models.AutoField(primary_key=True, serialize=False)),
                ('register_date', models.DateField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('expiration_date', models.DateField(default=datetime.date(2020, 12, 2), verbose_name='Duración')),
                ('client_id', models.OneToOneField(blank=True, db_column='client_id', on_delete=django.db.models.deletion.CASCADE, to='clients.clients', verbose_name='Cliente')),
                ('included_classes', models.ManyToManyField(blank=True, null=True, to='clients.GYMCLASSES', verbose_name='Clases incluidas')),
            ],
            options={
                'verbose_name': 'Membresía',
                'db_table': 'MEMBERSHIPS',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GROUPS',
            fields=[
                ('group_id', models.AutoField(primary_key=True, serialize=False)),
                ('weekday', models.CharField(choices=[('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miércoles', 'Miércoles'), ('Jueves', 'Jueves'), ('Viernes', 'Viernes'), ('Sábado', 'Sábado'), ('Domingo', 'Domingo')], max_length=15, verbose_name='Día')),
                ('hour', models.CharField(max_length=10, null=True, verbose_name='Hora')),
                ('gymclass_id', models.ForeignKey(db_column='gymclass_id', on_delete=django.db.models.deletion.DO_NOTHING, to='clients.gymclasses', verbose_name='Clase')),
                ('trainer_id', models.ForeignKey(blank=True, db_column='trainer_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='clients.trainers', verbose_name='Entrenador')),
            ],
            options={
                'verbose_name': 'Grupo',
                'db_table': 'GROUPS',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CLIENTS_ATTENDANCES',
            fields=[
                ('attendance_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('client_id', models.ForeignKey(blank=True, db_column='client_id', on_delete=django.db.models.deletion.DO_NOTHING, to='clients.clients', verbose_name='Cliente')),
            ],
            options={
                'db_table': 'CLIENT_ATTENDANCES',
                'managed': True,
            },
        ),
    ]
