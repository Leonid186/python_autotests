import requests

#переменные
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'fa0b8a2cf48761712ddd9285afbd970a'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN }

#Создать покемона
body_create = {
    "name": "Gigant",
    "photo_id": 4
}

# Смена имени покемона
body_change_name = {
    "pokemon_id": "167551",
    "name": "Atlas",
    "photo_id": 4
}

# Поймать покемона
body_add_pokeball = {
    "pokemon_id": "167551"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_change_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name)
print(response_change_name.text)'''

'''response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)'''