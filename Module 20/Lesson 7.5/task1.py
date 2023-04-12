def prepare_list_to_tuple(f_string):
    f_list = "".join(f_string.split()).split(',')
    f_search_list = [int(item) for item in f_list if item.isdigit()]
    return tuple(f_search_list), tuple(f_list)


data = {
    (5000, 123456): ('Иванов', 'Василий'),
    (6000, 111111): ('Иванов', 'Петр'),
    (7000, 222222): ('Медведев', 'Алексей'),
    (8000, 333333): ('Алексеев', 'Георгий'),
    (9000, 444444): ('Георгиева', 'Мария')
}

passport = input('Введите серию и номер паспорта через запятую:')

while ',' not in passport:
    print('Большая просьба ввести серию и номер паспорта в формате NNNN, NNNNNN,')
    print('где N - цифры серии и номера Вашего паспорта. Например 1234, 567890. Попробуйте снова: ')
    passport = input('Введите серию и номер паспорта через запятую:')

search_value, output_value = prepare_list_to_tuple(passport)

if search_value in data:
    print('\nВладелец паспорта серии: {serial}  номер: {number} найден:'.format(serial=output_value[0],
                                                                                number=output_value[1]))
    print('-----------------------------------------------------')
    print('Имя:', data[search_value][1])
    print('Фамилия:', data[search_value][0])
else:
    print('\nВладелец паспорта серии: {serial}  номер: {number} не найден.'.format(serial=output_value[0],
                                                                                   number=output_value[1]))
print('-----------------------------------------------------')
