phonebook = dict()
while True:
    print('\nТекущие контакты на телефоне:')
    if len(phonebook) == 0:
        print('<пусто>')
    else:
        for contact in phonebook:
            print(contact, phonebook[contact])
    name = input('\nВведите имя: ')
    if name == 'выход':
        break
    if name not in phonebook:
        phonebook[name] = input('Введите номер телефона: ')
    else:
        print('Ошибка: такое имя уже существует.')
