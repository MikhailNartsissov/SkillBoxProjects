from math import pi


def area(f_radius, f_height):
    f_side = 2 * pi * f_radius * f_height
    f_full = f_side + 2 * pi * f_radius ** 2
    return f_side, f_full


radius = int(input('Введите значение радиуса цилиндра: '))
height = int(input('Введите значение высоты цилиндра: '))

side, full = area(radius, height)

print('\nПлощадь боковой поверхности такого цилиндра составляет: ', side)
print('Общая площадь поверхности такого цилиндра составляет: ', full)
