from django.db import models

# Create your models here.

class MEMBERSHIPS(models.Model):
    membership_id = models.AutoField(primary_key=True)
    register_date = models.DateField()
    expiration_date = models.DateField()

    class Meta:
        managed = True
        db_table = 'MEMBERSHIPS'

class CLIENTS(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=40, blank=True, null=False)
    client_surname = models.CharField(max_length=40, blank=True, null=True)
    client_birthday = models.DateField()
    client_phone = models.IntegerField(blank=True, null=True)
    clietn_emergency_phone = models.IntegerField(blank=True)
    client_email = models.CharField(max_length=40, blank=True, null=True)
    client_gender = models.CharField(max_length=1, blank=True, null=True)
    membership_id = models.ForeignKey('MEMBERSHIPS', models.DO_NOTHING, db_column='membership_id', blank=True)

    class Meta:
        managed = True
        db_table = 'CLIENTS'

class GYMCLASSES(models.Model):
    gymclass_id = models.AutoField(primary_key=True)
    gymclass_name = models.CharField(max_length=40, blank=True)
    class Meta:
        managed = True
        db_table = 'GYMCLASSES'

class TRAINERS(models.Model):
    trainer_id = models.AutoField(primary_key=True)
    trainer_name = models.CharField(max_length=40, blank=True)
    trainer_surname = models.CharField(max_length=40, blank=True, null=True)
    trainer_birthday = models.DateField()
    trainer_phone = models.IntegerField(blank=True, null=True)
    trainer_email = models.CharField(max_length=40, blank=True, null=True)
    trainer_gender = models.CharField(max_length=1, blank=True, null=True)
    trainer_address = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'TRAINNERS'

class WEEKDAYS(models.Model):
    weekdays_id = models.AutoField(primary_key=True)
    weekdays_name = models.CharField(max_length=15)
    
    class Meta:
        managed = True
        db_table = 'WEEKDAYS'

class HOURS(models.Model):
    hour_id = models.AutoField(primary_key=True)
    hour_name = models.CharField(max_length=20)
    
    class Meta:
        managed = True
        db_table = 'HOURS'

class GROUPS(models.Model):
    group_id = models.AutoField(primary_key=True)
    gymclass_id = models.ForeignKey('GYMCLASSES', models.DO_NOTHING, db_column='gymclass_id', blank=True, null=True)
    trainer_id = models.ForeignKey('TRAINERS', models.DO_NOTHING, db_column='trainer_id', blank=True, null=True)
    weekday_id = models.ForeignKey('WEEKDAYS', models.DO_NOTHING, db_column='weekdays_id', blank=True, null=True)
    hour_id = models.ForeignKey('HOURS', models.DO_NOTHING, db_column='hour_id', blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'GROUPS'

    