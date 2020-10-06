from django import forms
from django.forms import ModelForm

from clients.models import *
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class MembershipForm(forms.ModelForm):
    class Meta:
        model = MEMBERSHIPS
        fields = '__all__'
        widgets = {
            'included_classes': forms.CheckboxSelectMultiple,
        }

class trainerForm(forms.ModelForm):
    trainer_password=forms.CharField(widget=forms.PasswordInput,validators=[validate_password],label="Contraseña")
    class Meta:
        model = TRAINERS
        fields=('trainer_name','trainer_surname','trainer_birthday','trainer_phone','trainer_emergency_phone','trainer_email','trainer_gender','trainer_address','trainer_rfc','trainer_password','trainer_rfid')

class trainerFormEdit(forms.ModelForm):

    class Meta:
        fields = '__all__'
        model=TRAINERS
        widgets = {
            'trainer_password': forms.PasswordInput
        }


class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Usuario', min_length=4, max_length=150)
    email = forms.EmailField(label='Email')
    is_superuser = forms.IntegerField(label="Admin")
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
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Este email ya ha sido registrado.")
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
        print("SAVING "*10)
        user = User.objects.get(username=self.cleaned_data.get('username'))
        isu = self.cleaned_data.get('is_superuser')
        print(isu)
        user.is_superuser = isu
        user.save()
        return user
