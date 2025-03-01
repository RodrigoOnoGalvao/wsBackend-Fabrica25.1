from django.shortcuts import render
import requests
from .models import Moeda

def Comparar_Moeda(request):
    url = 'https://data.fixer.io/api/latest?access_key=01b2f336a27b597b50c6e31a564e90a3'
    response = requests.get(url)
    dados = response.json()
    moedas = Moeda.objects.all()
    context = {
        'moedas': moedas,
        'dados': dados
    }
    return render(request, 'app/comparar_moeda.html', context)

# Create your views here.
