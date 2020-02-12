from django import forms
from .models import Pokemon

class PokemonForm(forms.ModelForm):
    first_pick = forms.CharField(required=True,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control', 'placeholder': 'First Pokemon'}))
    second_pick = forms.CharField(required=True,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control', 'placeholder': 'Second Pokemon'}))

    class Meta:
        model = Pokemon
        fields = []
