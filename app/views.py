from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import render
from .models import Pessoa, Moeda
from .forms import PessoaForm, MoedaForm
import requests


def index(request):
    return render(request, 'index.html')
# Fetch exchange rates from Fixer.io
def atualizar_moedas():
    api = 'https://data.fixer.io/api/latest?access_key=01b2f336a27b597b50c6e31a564e90a3'
    response = requests.get(api)
    data = response.json()
    moedas = []
    for sigla, valor in data['rates'].items():
        moeda = Moeda.objects.all(nome='Euro', sigla=sigla, valor=valor)
        moedas.append(moeda)
    return moedas
# Moeda Views
class MoedaListView(ListView):
    model = Moeda
    template_name = "moeda/moeda_list.html"
    context_object_name = "moedas"

class MoedaCreateView(CreateView):
    model = Moeda
    form_class = MoedaForm
    template_name = "moeda/moeda_form.html"
    success_url = reverse_lazy("moeda_list")

class MoedaUpdateView(UpdateView):
    model = Moeda
    form_class = MoedaForm
    template_name = "moeda/moeda_form.html"
    success_url = reverse_lazy("moeda_list")

class MoedaDeleteView(DeleteView):
    model = Moeda
    template_name = "moeda/moeda_confirm_delete.html"
    success_url = reverse_lazy("moeda_list")

class MoedaDetailView(DetailView):
    model = Moeda
    template_name = "moeda/moeda_detail.html"
    success_url = reverse_lazy("moeda_list")

# Pessoa Views
class PessoaListView(ListView):
    model = Pessoa
    template_name = "pessoa/pessoa_list.html"
    context_object_name = "pessoas"

class PessoaCreateView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    template_name = "pessoa/pessoa_form.html"
    success_url = reverse_lazy("pessoa_list")

class PessoaUpdateView(UpdateView):
    model = Pessoa
    form_class = PessoaForm
    template_name = "pessoa/pessoa_form.html"
    success_url = reverse_lazy("pessoa_list")

class PessoaDeleteView(DeleteView):
    model = Pessoa
    template_name = "pessoa/pessoa_confirm_delete.html"
    success_url = reverse_lazy("pessoa_list")

class PessoaDetailView(DetailView):
    model = Pessoa
    template_name = "pessoa/pessoa_detail.html"
    success_url = reverse_lazy("pessoa_list")
