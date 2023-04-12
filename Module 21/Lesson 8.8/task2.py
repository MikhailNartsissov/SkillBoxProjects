def ask_user(f_question='Хотите ввести максимальную глубину Y/N?',
             f_err_msg='Пожалуйста, введите Y или N (можно Д или Н)',
             f_retries=3):
    while f_retries > 0:
        f_answer = input(f_question).strip().lower()
        if f_answer == 'y' or f_answer == 'д':
            return True
        elif f_answer == 'n' or f_answer == 'н':
            return False
        else:
            f_retries -= 1
            print(f_err_msg)
    print('Превышено максимально допустимое число попыток. Используется значение по умолчанию.')
    return False


def value_by_key(f_dict, f_key, f_depth=3):
    if f_key in f_dict.keys() and f_depth > 0:
        return f_dict[f_key]
    for f_subdict in f_dict.values():
        if isinstance(f_subdict, dict):
            f_search_value = value_by_key(f_subdict, f_key, f_depth=f_depth - 1)
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

key_to_find = input('Введите искомый ключ: ')

if ask_user():

    max_depth = int(input('Введите максимальную глубину: '))
    while max_depth <= 0 or max_depth > 3:
        print('Максимальная глубина поиска не может быть меньше 1 или больше 3. Попробуйте снова.', end=' ')
        max_depth = int(input('Введите максимальную глубину: '))

    value = value_by_key(site, key_to_find, f_depth=max_depth)
else:
    value = value_by_key(site, key_to_find)

print('Значение ключа:', value)
