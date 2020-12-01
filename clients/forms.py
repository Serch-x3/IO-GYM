from django import forms
from django.forms import ModelForm

from clients.models import *
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_slug

validate_letters = RegexValidator(r'^[a-zA-Z]*$', 'Sólo se permiten letras')
validate_alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Sólo se permiten carácteres alfanuméricos (0-9 y A-Z).')

class MembershipForm(forms.ModelForm):
    class Meta:
        model = MEMBERSHIPS
        fields = '__all__'
        widgets = {
            'included_classes': forms.CheckboxSelectMultiple,
        }


class trainerForm(forms.ModelForm):
    trainer_password=forms.CharField(widget=forms.PasswordInput,validators=[validate_password],label="Contraseña")
    trainer_password2=forms.CharField(widget=forms.PasswordInput,validators=[validate_password],label="Confirmación de contraseña")
    class Meta:
        model = TRAINERS
        fields=('trainer_name','trainer_surname','trainer_birthday','trainer_phone','trainer_emergency_phone','trainer_email','trainer_gender','trainer_address','trainer_rfc','trainer_password','trainer_rfid')

    def clean_trainer_rfid(self):
        rfid = self.cleaned_data.get('trainer_rfid')
        if TRAINERS.objects.filter(trainer_rfid = rfid).count() > 0:
            raise ValidationError("Esta llave de acceso ya ha sido registrado. Use otro.")
        return rfid

    def clean_trainer_password2(self):
        password1 = self.cleaned_data.get('trainer_password')
        password2 = self.cleaned_data.get('trainer_password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no coiciden.")

        return password2



class trainerFormEdit(forms.ModelForm):
    trainer_password=forms.CharField(widget=forms.PasswordInput,validators=[validate_password],label="Contraseña")
    trainer_password2=forms.CharField(widget=forms.PasswordInput,validators=[validate_password],label="Confirmación de contraseña")


    class Meta:
        model = TRAINERS
        #fields = ('trainer_id','trainer_name','trainer_surname','trainer_birthday','trainer_phone','trainer_emergency_phone','trainer_email','trainer_gender','trainer_address','trainer_rfc','trainer_password','trainer_rfid')
        fields = ('__all__')

    def clean_trainer_password2(self):
        password1 = self.cleaned_data['trainer_password']
        password2 = self.cleaned_data['trainer_password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no coiciden.")

        return password2

    def clean_trainer_rfid(self):
        print("X"*60)
        print(self.initial['trainer_id'])
        rfid = self.cleaned_data.get('trainer_rfid')
        if TRAINERS.objects.get(trainer_id = self.initial['trainer_id']).trainer_rfid != rfid:
            print("RFID DIFERENTE")
            if TRAINERS.objects.filter(trainer_rfid = rfid).count() > 0:
                print("RFID EN OTRO REGISTRO")
                raise ValidationError("Esta llave de acceso ya ha sido registrado. Use otro.")
        print("RFID TERMINADO")
        return rfid



class trainerFormEditWithoutPassword(forms.ModelForm):

    class Meta:
        model = TRAINERS
        fields = ('trainer_id','trainer_name','trainer_surname','trainer_birthday','trainer_phone','trainer_emergency_phone','trainer_email','trainer_gender','trainer_address','trainer_rfc','trainer_rfid')


    def clean_trainer_rfid(self):
        print("X"*60)
        print(self.initial['trainer_id'])
        rfid = self.cleaned_data.get('trainer_rfid')
        if TRAINERS.objects.get(trainer_id = self.initial['trainer_id']).trainer_rfid != rfid:
            print("RFID DIFERENTE")
            if TRAINERS.objects.filter(trainer_rfid = rfid).count() > 0:
                print("RFID EN OTRO REGISTRO")
                raise ValidationError("Esta llave de acceso ya ha sido registrado. Use otro.")
        print("RFID TERMINADO")
        return rfid





class CustomUserCreationForm(forms.Form):
    is_superuser = forms.IntegerField(label="Admin")
    username = forms.CharField(label='Usuario', min_length=4, max_length=150, validators=[validate_alphanumeric])
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmación de contraseña', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Este usuario ya existe.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        is_superuser = self.cleaned_data['is_superuser']
        r = User.objects.filter(email=email)
        if r.count() == 1:
            r = User.objects.get(email=email)
            if r.is_superuser == is_superuser:
                if is_superuser == 0:
                    raise  ValidationError("Este email ya ha sido registrado en un usuario de tipo asistente. Sólo puede crear una más de tipo administrador")
                else:
                    raise  ValidationError("Este email ya ha sido registrado en un usuario de tipo administrador. Sólo puede crear una más de tipo asistente")
        elif r.count() == 2:
            raise  ValidationError("Este email ya ha sido registrado como administrador y asistente. Utilice otro email.")

        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no coiciden.")

        return password2

    def save(self, commit=True):
        if self.cleaned_data['is_superuser'] == 1:
            user = User.objects.create_superuser(
                self.cleaned_data['username'],
                self.cleaned_data['email'],
                self.cleaned_data['password1']
            )
        else:
            user = User.objects.create_user(
                self.cleaned_data['username'],
                self.cleaned_data['email'],
                self.cleaned_data['password1']
            )
        return user




class CustomUserEditFormWithPassword(forms.Form):
    username = forms.CharField(label='Usuario', min_length=4, max_length=150)
    is_superuser = forms.IntegerField(label="Admin")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmación de contraseña', widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        #WHEN IS BLANK OBTAIN THE CURRENT PASSWORD

        if password1 != password2:
            raise ValidationError("Las contraseñas no coiciden.")

        return password2

    def save(self, commit=True):
        print("SAVING "*10)
        user = User.objects.get(username=self.cleaned_data.get('username'))
        pw = self.cleaned_data.get('password1')
        isu = self.cleaned_data.get('is_superuser')
        user.is_superuser = isu
        if not pw == '':
            user.set_password(pw)
        user.save()
        return user


class CustomUserEditForm(forms.Form):
    username = forms.CharField(label='Usuario', min_length=4, max_length=150)
    is_superuser = forms.IntegerField(label="Admin")

    def save(self, commit=True):
        user = User.objects.get(username=self.cleaned_data.get('username'))
        isu = self.cleaned_data.get('is_superuser')
        user.is_superuser = isu
        user.save()
        return user
