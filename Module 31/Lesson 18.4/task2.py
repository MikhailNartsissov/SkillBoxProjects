from requests import get
from json import loads, dump
from time import sleep

data = get('https://swapi.dev/api/planets/1/?format=wookiee')
wookiee_planet = loads(data.text)
with open('wookiee_planet.json', 'w', encoding='utf-8') as file:
    dump(wookiee_planet, file, indent=4)

data = get('https://swapi.dev/api/films/?search=A New Hope')
film = loads(data.text)['results'][0]['opening_crawl']


for item in film:
    print(item, end='')
    sleep(0.01)
with open('film.json', 'w', encoding='utf-8') as file:
    dump(film, file, indent=4)
