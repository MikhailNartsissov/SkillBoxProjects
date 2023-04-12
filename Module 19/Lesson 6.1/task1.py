max_num_for_square = int(input('Введите целое число: '))
squares = dict()
for squares_index in range(1,max_num_for_square +1):
    squares[squares_index] = squares_index ** 2
print('Результат: ', squares)
