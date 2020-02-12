import requests

# The pokemon_data function accepts a pokemon name string as an argument and returns a list containing the pokemon type as well as base stats.
def pokemon_data(pokemon):
    url = "http://pokeapi.co/api/v2/pokemon/" + pokemon + "/"
    response = requests.request("GET", url)
    data = response.json()
    pokemon_info = []
    pokemon_info.append(data['types'][0]['type']['name'])
    pokemon_info.append(data['stats'][0]['base_stat'])
    return pokemon_info

#The process_poke_comparison compares the two pokemon inputted by the user.
def process_poke_comparison(pokemon1, pokemon2):
    first_pick = pokemon_data(pokemon1)
    second_pick = pokemon_data(pokemon2)
    url = "https://pokeapi.co/api/v2/type"
    response = requests.request("GET", url)
    data = response.json()
    type = first_pick[0]
    type_vs = second_pick[0]

    #Get the API URL for the specific type of pokemon.
    for point in data['results']:
        if point['name'] == type:
            strength_url = point['url']

    #Default to false for base stats being equal, which will change if that condition is reached.
    pokemon_same_base = False
    response = requests.request("GET", strength_url)
    data = response.json()

    test_counter=0

    #Check if the second pokemon argument is strong against the first pokemon argument type.
    for weakness in data['damage_relations']['double_damage_from']:
        if (weakness['name']) == type_vs:
            test_counter=test_counter - 1
            break

    #Check the same as above for weaknesses.
    for strength in data['damage_relations']['double_damage_to']:
        if (strength['name']) == type_vs:
            test_counter = test_counter + 1
            break

    if test_counter == 0:
        if (first_pick[1] > second_pick[1]):
            win_battle = True
        if (second_pick[1] > first_pick[1]):
            win_battle = False
        if (second_pick[1] == first_pick[1]):
            pokemon_same_base = True
    if test_counter > 0:
        win_battle=True
    if test_counter < 0:
        win_battle=False
    print(test_counter)
    # Printing for debugging
    print(pokemon1)
    print(first_pick)
    print(pokemon2)
    print(second_pick)

    if pokemon_same_base == True:
        return pokemon1
    else:
        if win_battle == True:
            return pokemon1
        else:
            return pokemon2
