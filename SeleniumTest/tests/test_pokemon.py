import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8105b86a5eb0194fc4d20d93122d512c'
HEADER ={'Content-Type': 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '5363'
PARAMS = {'trainer_id':TRAINER_ID}


def test_status_code():
    response= requests.get(url=f'{URL}/trainers', params=PARAMS)
    assert response.status_code == 200
    
def test_contains_name():
    response_get = requests.get(url=f'{URL}/trainers', params=PARAMS)
    assert response_get.json()['data'][0]['trainer_name']=='Yana'