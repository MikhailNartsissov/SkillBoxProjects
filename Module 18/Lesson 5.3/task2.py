congrats_text = input('Введите шаблон поздравления, '
                      'в шаблоне нужно использовать конструкции '
                      '{name} и {age}: ')
while not ('{name}' in congrats_text) or not ('{age}' in congrats_text):
    print('Ошибка. Отсутствует одна или обе конструкции {name}/{age}')
    congrats_text = input('Введите шаблон поздравления, '
                          'в шаблоне нужно использовать конструкции '
                          '{name} и {age}: ')

names_list = input('Введите список имён через запятую: ').split(', ')
ages_list = input('Введите список возрастов людей через пробел: ').split()

print()
for i_man in range(len(names_list)):
    print(congrats_text.format(name=names_list[i_man], age=ages_list[i_man]))

people = [
    ' '.join(
        [
            names_list[i_man],
            ages_list[i_man]
        ]
    )
    for i_man in range(len(names_list))]

people = ', '.join(people)

print('\nИменинники: ', people)
