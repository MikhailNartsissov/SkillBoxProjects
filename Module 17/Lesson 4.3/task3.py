from random import randint

squad_1 = [randint(50, 80) for _ in range(10)]
squad_2 = [randint(30, 60) for _ in range(10)]
squad_3 = ['Погиб' if squad_1[i_unit] + squad_2[i_unit] > 100 else 'Выжил' for i_unit in range(10)]

print('Урон, наносимый юнитами первого отряда:', squad_1)
print('Урон, наносимый юнитами второго отряда:', squad_2)
print('Состояние юнитов третьего отряда после атаки:', squad_3)
