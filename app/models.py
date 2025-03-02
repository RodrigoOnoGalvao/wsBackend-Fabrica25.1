from django.db import models

class Moeda(models.Model):
    nome = models.CharField(max_length=50)
    codigo = models.CharField(max_length=3, unique=True)  # e.g., "USD", "EUR"
    taxa_conversao = models.DecimalField(max_digits=10, decimal_places=4)  # Exchange rate

    def __str__(self):
        return f"{self.nome} ({self.codigo})"

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    moeda_preferida = models.ForeignKey(Moeda, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome
