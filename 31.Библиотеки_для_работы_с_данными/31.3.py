"""Задача 3. May the force be with you
Что нужно сделать
Фанаты «Звёздных войн» (Star Wars) написали API по своей любимой вселенной. Ссылка на документацию: Documentation.

Внимательно изучите документацию этого API и напишите программу, которая выводит на экран (и в JSON-файл) информацию
о пилотах легендарного корабля Millennium Falcon.

Информация о корабле должна содержать следующие пункты:

название,
максимальная скорость,
класс,
список пилотов.
Внутри списка о каждом пилоте должна быть следующая информация:

имя,
рост,
вес,
родная планета,
ссылка на информацию о родной планете.
Пример вывода информации по кораблю X-wing в консоль:"""

import requests
import json


url = requests.get('https://swapi.dev/api/starships/10/')
data = url.json()

pilots = []

for pilot in data['pilots']:
    pilot_req = requests.get(pilot)
    pilot_data = pilot_req.json()
    homeworld_req = requests.get(pilot_data['homeworld'])
    homeworld_data = homeworld_req.json()
    pilot_info = {
        'name': pilot_data['name'],
        'height': pilot_data['height'],
        'mass': pilot_data['mass'],
        'homeworld': {
            'name': homeworld_data['name'],
            'url': pilot_data['homeworld']
        }
    }
    pilots.append(pilot_info)

ship_info = {
    'name': data['name'],
    'max_speed': data['max_atmosphering_speed'],
    'class': data['starship_class'],
    'pilots': pilots
}

print(json.dumps(ship_info, indent=4))

with open('millennium_falcon.json', 'w') as file:
    json.dump(ship_info, file, indent=4)