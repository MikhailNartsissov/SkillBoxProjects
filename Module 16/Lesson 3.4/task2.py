participants_quantity = int(input('Кол-во участников: '))
team_members_quantity = int(input('Кол-во человек в команде: '))
first_member_index = 1
team_list = []

if participants_quantity % team_members_quantity == 0:
    for _ in range(participants_quantity // team_members_quantity):
        team_list.append(list(range(first_member_index, first_member_index + team_members_quantity)))
        first_member_index += team_members_quantity
else:
    print(participants_quantity, 'участников невозможно поделить на команды по', team_members_quantity, 'человек!')

# for _ in range(participants_quantity // team_members_quantity):
#     team_list.append(list(range(first_member_index, first_member_index + team_members_quantity)))
#     first_member_index += team_members_quantity
# team_list.append(list(range(first_member_index, first_member_index + participants_quantity % team_members_quantity)))
# print('\nОбщий список команд:', team_list, sep='')
