from django import forms
from .models import Memeber   

class MemeberForm(forms.ModelForm):
    class Meta:
        model = Memeber
        fields = ['name', 'email', 'contact']

        