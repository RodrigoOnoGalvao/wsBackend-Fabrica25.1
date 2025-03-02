from django.contrib import admin
from .models import Pessoa, Moeda

admin.site.register(Pessoa)
admin.site.register(Moeda)

class MoedaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo', 'taxa_conversao')
    search_fields = ('nome', 'codigo')
    filter_horizontal = ('pessoas',)
    ordering = ('nome',)
    


class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'moeda_preferida')
    search_fields = ('nome', 'email')