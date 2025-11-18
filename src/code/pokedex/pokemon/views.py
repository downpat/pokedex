import json
import requests

from django.http import HttpResponse
from django.shortcuts import render

from .models import Pokemon
from .tasks import load_pokemon


def index(request):
    return render(request, 'index.html', {})

def build_pokedex(request):
    pokemon = Pokemon.objects.all()

    if len(pokemon) < 500:
        pokemon.delete()
        resp = requests.get('https://pokeapi.co/api/v2/pokemon/?limit=1400')
        resp_dict = json.loads(resp.content)
        poke_pairs = resp_dict['results']

        for pair in poke_pairs:
            load_pokemon.delay(
                pair['name'],
                pair['url']
            )

        return render(request, 'build.html', {})

    return render(request, 'no_build.html', {})

def full_list(request):
    pokemon = Pokemon.objects.all()
    return render(request, 'pokemon_list.html', {
        "count": len(pokemon),
        "pokemon": pokemon
    })

def single_pokemon(request, name):
    pokemon = Pokemon.objects.get(name=name)
    return render(request, 'pokemon.html', {"pokemon": pokemon})
