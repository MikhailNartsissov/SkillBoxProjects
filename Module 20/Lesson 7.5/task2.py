name = ''
phonebook = dict()
choice = ''
while name.lower() != 'хватит':
    name = input('Введите имя контакта (\'хватит\' для завершения работы): ')
    if name.lower() == 'хватит':
        print('Всего Вам доброго! Хорошего дня.')
        break
    surname = input('Введите фамилию контакта: ')
    phone = input('Введите номер телефона контакта: ')
    if (name, surname) not in phonebook:
        phonebook[(name, surname)] = phone
    else:
        print('ВНИМАНИЕ! {0} {1} уже есть в списке. Обновить номер телефона y/n или д/н? '.format(name, surname),
              end='')
        choice = input().lower()
        while choice != 'y' and choice != 'n' and choice != 'д' and choice != 'н':
            print('Введено недопустимое значение выбора. Введите y/n или д/н', end=' ')
            choice = input().lower()
        if choice == 'y' or choice == 'д':
            phonebook[(name, surname)] = phone
    print('\nТекущий словарь контактов:')
    for key, value in phonebook.items():
        print('Имя:', key[0])
        print('Фамилия:', key[1])
        print('Номер телефона:', value, '\n')
