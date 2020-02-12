from django.shortcuts import render
from .models import Pokemon
from .forms import PokemonForm
from . import call_pokeapi


# Create your views here.

def pokecheck(request):
    result='Not Valid'
    print('1')
    if request.method == "POST":
        print('2')
        pokemon_choices = PokemonForm(request.POST)
        print(pokemon_choices)
        if pokemon_choices.is_valid():
            print('3')
            first_pick = pokemon_choices.cleaned_data['first_pick']
            second_pick = pokemon_choices.cleaned_data['second_pick']
            result=call_pokeapi.process_poke_comparison(first_pick, second_pick)
            print(result)
        else:
            result='Still Invalid'
            print(result)

    else:
        pokemon_choices=PokemonForm()
        result='Invalid Data'
        print(result)
    return render(request, "pokecheck/checker.html", {'pokemon_choices':pokemon_choices, 'result': result})