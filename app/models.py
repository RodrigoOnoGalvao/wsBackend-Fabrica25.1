from django.db import models

class Moeda(models.Model):
    nome = models.CharField(max_length=3)
    valor = models.DecimalField(max_digits=15, decimal_places=15)
    def __str__(self):
        return f"{self.nome} - {self.valor}"
    

# Create your models here.
