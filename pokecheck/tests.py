from django.test import TestCase
from .models import Pokemon
from . import call_pokeapi

# Create your tests here.

class PokemonTest(TestCase):
    def setUp(self):
        Pokemon.objects.create(first_pick="pikachu", second_pick="charmander")
    def test_animals_can_speak(self):
        pokemon_set=Pokemon.objects.get(first_pick='pikachu')
        self.assertEqual(pokemon_set.second_pick == 'charmander', pokemon_set.first_pick== 'pikachu')
