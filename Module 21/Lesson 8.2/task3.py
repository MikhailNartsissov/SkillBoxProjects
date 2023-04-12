def my_value_by_key(f_dict, f_key):
    if f_key in f_dict.keys():
        return f_dict[f_key]
    for f_subdict in f_dict.values():
        if isinstance(f_subdict, dict):
            f_search_value = my_value_by_key(f_subdict, f_key)
            if f_search_value:
                break
    else:
        return None
    return f_search_value


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

key_to_find = input('Введите ключ для поиска: ')
value = my_value_by_key(site, key_to_find)
if value:
    print(value)
else:
    print('Такого ключа в структуре нет.')
