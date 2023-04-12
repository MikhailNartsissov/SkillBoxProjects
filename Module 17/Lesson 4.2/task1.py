left_border = int(input('Введите значение левой границы диапазона: '))
right_border = int(input('Введите значение правой границы диапазона: '))
print('\nЗначения в кубе: ', [element ** 3 for element in range(left_border, right_border + 1)])
print('Значения в квадрате: ', [element ** 2 for element in range(left_border, right_border + 1)])
