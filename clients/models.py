from django.db import models
# Create your models here.

class clientesView(models.Model):
    id=models.CharField(),
    date=models.DateField();

    class Meta:
        managed = False
        db_table = 'clientesView'

class MEMBERSHIPS(models.Model):
    membership_id = models.AutoField(primary_key=True)
    register_date = models.DateField()
    expiration_date = models.DateField()
    client_id = models.ForeignKey('CLIENTS', models.DO_NOTHING, db_column='client_id', blank=True)
    membership_type_id = models.ForeignKey('MEMBERSHIP_TYPES', models.DO_NOTHING, db_column='membership_type_id', blank=True)

    class Meta:
        managed = True
        db_table = 'MEMBERSHIPS'

    def __str__(self):
        return self.client_id

class MEMBERSHIP_TYPES(models.Model):
    membership_type_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=60, blank=True, null=False)

    def __str__(self):
        return self.description

    class Meta:
        managed = True
        db_table = 'MEMBERSHIP_TYPES'

class CLASS_TYPES(models.Model):
    class_type_id = models.AutoField(primary_key=True)
    membership_type_id = models.ForeignKey('MEMBERSHIP_TYPES', models.DO_NOTHING, db_column='membership_type_id', blank=True)
    gymclass_id = models.ForeignKey('GYMCLASSES', models.DO_NOTHING, db_column='gymclass_id', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'CLASS_TYPES'


class CLIENTS_ATTENDANCES(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey('CLIENTS', models.DO_NOTHING, db_column='client_id', blank=True, null=False)
    date = models.DateField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'CLIENT_ATTENDANCES'


class TRAINERS_ATTENDANCES(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    trainer_id = models.ForeignKey('TRAINERS', models.DO_NOTHING, db_column='trainer_id', blank=True)
    date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=10, blank=True, null=False)

    class Meta:
        managed = True
        db_table = 'TRAINNERS_ATTENDANCES'

class CLIENTS(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=40, blank=True, null=False)
    client_surname = models.CharField(max_length=40, blank=True, null=True)
    client_birthday = models.DateField()
    client_phone = models.IntegerField(blank=True, null=True)
    client_emergency_phone = models.IntegerField(blank=True)
    client_email = models.CharField(max_length=40, blank=True, null=True)
    client_gender = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'CLIENTS'

    def __str__(self):
        return self.client_name+' '+self.client_surname

class GYMCLASSES(models.Model):
    gymclass_id = models.AutoField(primary_key=True)
    gymclass_name = models.CharField(max_length=40, blank=True)
    class Meta:
        managed = True
        db_table = 'GYMCLASSES'
    def __str__(self):
        return self.gymclass_name

class TRAINERS(models.Model):
    trainer_id = models.AutoField(primary_key=True)
    trainer_name = models.CharField(max_length=40, blank=True)
    trainer_surname = models.CharField(max_length=40, blank=True, null=True)
    trainer_birthday = models.DateField()
    trainer_phone = models.IntegerField(blank=True, null=True)
    trainer_email = models.CharField(max_length=40, blank=True, null=True)
    trainer_gender = models.CharField(max_length=1, blank=True, null=True)
    trainer_address = models.CharField(max_length=60, blank=True, null=True)
    trainer_emergency_phone = models.IntegerField(blank=True)
    trainer_rfc = models.CharField(max_length=13, blank=True, null=True)
    trainer_password = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = True
        db_table = 'TRAINNERS'

    def __str__(self):
        return self.trainer_name+' '+self.trainer_surname

class WEEKDAYS(models.Model):
    weekdays_id = models.AutoField(primary_key=True)
    weekdays_name = models.CharField(max_length=15)

    class Meta:
        managed = True
        db_table = 'WEEKDAYS'

    def __str__(self):
        return self.weekdays_name

class HOURS(models.Model):
    hour_id = models.AutoField(primary_key=True)
    hour_name = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'HOURS'
    def __str__(self):
        return self.hour_name


class GROUPS(models.Model):
    group_id = models.AutoField(primary_key=True)
    gymclass_id = models.ForeignKey('GYMCLASSES', models.DO_NOTHING, db_column='gymclass_id', blank=True, null=True)
    trainer_id = models.ForeignKey('TRAINERS', models.DO_NOTHING, db_column='trainer_id', blank=True, null=True)
    weekday_id = models.ForeignKey('WEEKDAYS', models.DO_NOTHING, db_column='weekdays_id', blank=True, null=True)
    hour_id = models.ForeignKey('HOURS', models.DO_NOTHING, db_column='hour_id', blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'GROUPS'
