from requests import get
from copy import copy
from json import loads, dump, dumps

starship_data = get('https://swapi.dev/api/starships/?search=Millennium Falcon')
starship_result_info = dict()
if starship_data.status_code == 200:
    starship_text = loads(starship_data.text)['results'][0]
    for key, value in starship_text.items():
        if key in ['name', 'max_atmosphering_speed', 'starship_class', 'pilots']:
            starship_result_info[key] = value
    pilots_url = copy(starship_result_info['pilots'])
    for url in pilots_url:
        pilot_data = get(url)
        if pilot_data.status_code == 200:
            pilot_result = dict()
            for key, value in loads(pilot_data.text).items():
                if key in ['name', 'height', 'mass', 'homeworld']:
                    pilot_result[key] = value
                    if key == 'homeworld':
                        homeworld_data = get(value)
                        if homeworld_data.status_code == 200:
                            pilot_result['homeworld_url'] = value
                            pilot_result['homeworld'] = loads(homeworld_data.text)['name']
            starship_result_info['pilots'].append(pilot_result)
            starship_result_info['pilots'].remove(url)
    print(dumps(starship_result_info, indent=4))
with open('starship.json', 'w') as file:
    dump(starship_result_info, file, indent=4)
