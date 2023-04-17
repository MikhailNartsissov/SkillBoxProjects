from requests import get
from json import dump, loads

data = get('https://swapi.dev/api/people/3/')
person = loads(data.text)
person['name'] = 'Mikhail Nartsissov'
home_world_url = person['homeworld']
data = get(home_world_url)
home_world = loads(data.text)
species_url = person['species']
data = get(species_url)
species = loads(data.text)
with open('about_me.json', 'w', encoding='utf-8') as file:
    dump(person, file, indent=4)
with open('about_my_planet.json', 'w', encoding='utf-8') as file:
    dump(home_world, file, indent=4)
with open('about_my_species.json', 'w', encoding='utf-8') as file:
    dump(species, file, indent=4)
