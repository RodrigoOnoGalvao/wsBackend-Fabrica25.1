import requests
from .models import Moeda

def atualizar_moedas():
    url = "https://data.fixer.io/api/latest?access_key=01b2f336a27b597b50c6e31a564e90a3"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()

        if data.get("success"):
            for codigo, taxa in data["rates"].items():
                moeda, created = Moeda.objects.get_or_create(codigo=codigo, defaults={"nome": codigo, "taxa_conversao": taxa})
                if not created:
                    moeda.taxa_conversao = taxa
                    moeda.save()
        else:
            print("Error in API response:", data.get("error"))
    except requests.exceptions.RequestException as e:
        print("Error fetching data from Fixer.io:", e)
