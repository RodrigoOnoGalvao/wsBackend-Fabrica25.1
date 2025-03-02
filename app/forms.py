from django import forms
from .models import Pessoa, Moeda

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'email', 'moeda_preferida']

class MoedaForm(forms.ModelForm):
    class Meta:
        model = Moeda
        fields = ['nome', 'codigo', 'taxa_conversao']
