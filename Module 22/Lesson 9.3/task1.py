import os


first_group = open(os.path.join('task', 'group_1.txt'), 'r', encoding='utf-8')
summa = 0
diff = None
for i_person in first_group:
    info = i_person.split()
    if diff is None:
        diff = int(info[2])
    else:
        diff -= int(info[2])
    summa += int(info[2])
first_group.close()

second_group = open(os.path.join('task', 'Additional_info', 'group_2.txt'), 'r', encoding='utf-8')
compose = None
for i_person in second_group:
    info = i_person.split()
    if compose is None:
        compose = int(info[2])
    else:
        compose *= int(info[2])
second_group.close()

print('\nСумма очков участников первой группы:', summa)
print('Разность очков участников первой группы', diff)
print('Произведение очков участников второй группы:', compose)
