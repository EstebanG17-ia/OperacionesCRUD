from django.contrib import admin
from .models import Pokemon

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'tipo_1', 'tipo_2', 'vida', 'ataque', 'defensa')