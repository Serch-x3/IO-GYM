from django import forms
from clients.models import *
from django.contrib.auth.password_validation import validate_password


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
        fields=('trainer_name','trainer_surname','trainer_birthday','trainer_phone','trainer_emergency_phone','trainer_email','trainer_gender','trainer_address','trainer_rfc','trainer_password')

class trainerFormEdit(forms.ModelForm):

    class Meta:
        fields = '__all__'
        model=TRAINERS
        widgets = {
            'trainer_password': forms.PasswordInput
        }
