import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = ''
HEADER ={'Content-Type': 'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "Бука",
    "photo_id": 6
}



response_create = requests.post(url = f'{URL}/pokemons', headers= HEADER, json = body_create )
print(response_create.text)


ID = response_create.json()['id'] 
body_change_name = {
    "pokemon_id": ID,
    "name": "Винни",
    "photo_id": 6
}

response_new_name = requests.put(url = f'{URL}/pokemons', headers= HEADER, json = body_change_name)
print(response_new_name.text)


body_add_pockeball = {
    "pokemon_id": ID
}

response_add_pockeball=requests.post(url = f'{URL}/trainers/add_pokeball', headers=HEADER, json= body_add_pockeball)
print(response_add_pockeball.text)