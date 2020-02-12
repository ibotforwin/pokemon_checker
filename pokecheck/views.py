from django.shortcuts import render
from .models import Pokemon
from .forms import PokemonForm
from . import call_pokeapi


def pokecheck(request):
    result = 'Not Valid'
    if request.method == "POST":
        pokemon_choices = PokemonForm(request.POST)
        if pokemon_choices.is_valid():
            first_pick = pokemon_choices.cleaned_data['first_pick'].lower()
            second_pick = pokemon_choices.cleaned_data['second_pick'].lower()
            result = call_pokeapi.process_poke_comparison(first_pick, second_pick)
        else:
            result = 'Invalid Input'
    else:
        pokemon_choices = PokemonForm()
    return render(request, "pokecheck/checker.html", {'pokemon_choices': pokemon_choices, 'result': result})
