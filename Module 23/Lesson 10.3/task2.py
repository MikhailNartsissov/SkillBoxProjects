try:
    participants_quantity = int(input('Кол-во участников: '))
    team_members_quantity = int(input('Кол-во человек в команде: '))
except ValueError:
    print('Введены некорректные данные. Кол-во участников принимается равным нулю. Кол-во человек в команде '
          'принимается равным единице.')
    participants_quantity = 0
    team_members_quantity = 1
else:
    print('Кол-во участников:', participants_quantity, 'Кол-во человек в команде', team_members_quantity)
finally:
    print('Блок try - except - else - finally пройден.')
    first_member_index = 1
    team_list = []

if participants_quantity % team_members_quantity == 0:
    for _ in range(participants_quantity // team_members_quantity):
        team_list.append(list(range(first_member_index, first_member_index + team_members_quantity)))
        first_member_index += team_members_quantity
else:
    print(participants_quantity, 'участников невозможно поделить на команды по', team_members_quantity, 'человек!')

print('\nОбщий список команд:', team_list, sep='')
