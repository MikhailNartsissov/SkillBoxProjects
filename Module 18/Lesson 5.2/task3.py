first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
fourth = int(input('Введите четвертое число: '))

ip_address = '{0}.{1}.{2}.{3}'.format(first, second, third, fourth)
print('IP адрес = ', ip_address)
