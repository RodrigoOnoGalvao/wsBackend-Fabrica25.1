from django import forms
from .models import Moeda

class MoedaForm(forms.ModelForm):
    class Meta:
        model = Moeda
        fields = ['nome', 'valor']