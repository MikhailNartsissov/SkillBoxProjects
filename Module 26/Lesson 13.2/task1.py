from random import randint


iterator_length = randint(1, 20)
sample_list = [randint(-100, 100) for _ in range(iterator_length)]

sample_iter = iter(sample_list)

while True:
    try:
        print(next(sample_iter))
    except StopIteration:
        print('Числа в списке кончились.')
        break
