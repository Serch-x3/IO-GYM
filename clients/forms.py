from django import forms
from clients.models import *


class MembershipForm(forms.ModelForm):



    class Meta:
        model = MEMBERSHIPS
        fields = '__all__'
        widgets = {
            'included_classes': forms.CheckboxSelectMultiple,
        }
    
