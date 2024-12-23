# Задачи:
# 1. Проверь, что ответ запрос GET /trainers приходит с кодом 200; +
# 2. Проверь, что в ответе приходит строчка с именем твоего тренера +

import requests
import pytest

#переменные
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'fa0b8a2cf48761712ddd9285afbd970a'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN }
TRAINER_ID = '13149'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers' , params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200
def test_trainer_name():
    response_get = requests.get(url = f'{URL}/trainers' , params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == "WhiteHusky"