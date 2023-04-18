from json import load, dump

diff_list = ['services', 'staff', 'datetime']
with open('json_new.json', 'r', encoding='utf-8') as new_file:
    new_data = load(new_file)['data']

with open('json_old.json', 'r', encoding='utf-8') as old_file:
    old_data = load(old_file)['data']

result = dict()
for item in old_data['services']:
    for key in item.keys():
        if item[key] != new_data['services'][0][key]:
            result['services'] = new_data['services']
            break
for key in old_data['staff'].keys():
    if old_data['staff'][key] != new_data['staff'][key]:
        result[key] = new_data[key]
if old_data['datetime'] != new_data['datetime']:
    result['datetime'] = new_data['datetime']

print(result)

with open('result.json', 'w', encoding='utf-8') as result_file:
    dump(result, result_file, indent=4, ensure_ascii=False)
