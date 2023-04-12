left_border = int(input('Введите значение левой границы диапазона: '))
right_border = int(input('Введите значение правой границы диапазона: '))
print('\nЗначения чётных чисел в диапазоне: ', [element
                                                for element in range(left_border, right_border + 1)
                                                if element % 2 == 0])
