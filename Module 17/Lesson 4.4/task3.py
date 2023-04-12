from random import randint

items = randint(2, 10)
original_list = [randint(0, 100) for _ in range(items)]
print('Исходный список: ', original_list)
left_border = randint(0, items - 1)
right_border = randint(0, items - 1)
while left_border >= right_border:
    left_border = randint(0, items - 1)
    right_border = randint(0, items - 1)
print('\nУдаляем с ', left_border, '-го по ', right_border, '-й элементы.')
original_list[left_border:right_border + 1] = []
print('В результате получим список: ', original_list)
