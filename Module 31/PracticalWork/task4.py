from re import fullmatch

phone_list = ['9999999999', '999999-999', '99999x9999', 'a999999999', '999999999a', '0873422341', '8456789012']
name_list = ['первый', 'второй', 'третий', 'четвёртый', 'пятый', 'шестой', 'седьмой', 'восьмой', 'девятый', 'десятый']

for phone in phone_list:
    phone_index = phone_list.index(phone)
    if phone_index < len(name_list):
        phone_str = name_list[phone_index] + ' номер:'
    else:
        phone_str = str(phone_index + 1) + '-й номер:'
    if fullmatch(r'\b([89])\d{9}', phone):
        print(phone_str, 'всё в порядке.')
    else:
        print(phone_str, 'не подходит.')
