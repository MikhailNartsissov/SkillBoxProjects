from random import randint


first_tuple = [randint(0, 5) for _ in range(10)]
second_tuple = [randint(-5, 0) for _ in range(10)]

print(first_tuple)

first_tuple.extend(second_tuple)
first_tuple = tuple(first_tuple)
second_tuple = tuple(second_tuple)

print(second_tuple)
print(first_tuple)
print('Количество нулей:', first_tuple.count(0))
