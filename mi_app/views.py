from django.shortcuts import render
from .models import Pokemon

def home(request):
    pokemones = Pokemon.objects.all()
    return render(request, 'mi_app/index.html', {'pokemones': pokemones})