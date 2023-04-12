from random import randint


class Toyota:
    color = 'Red'
    price = 1000000
    max_speed = 200
    current_speed = 0


car1 = Toyota()
car2 = Toyota()
car3 = Toyota()
car1.current_speed = randint(0, 200)
car2.current_speed = randint(0, 200)
car3.current_speed = randint(0, 200)

print('Текущая скорость первой Тойоты равна:', car1.current_speed)
print('Текущая скорость второй Тойоты равна:', car2.current_speed)
print('Текущая скорость третьей Тойоты равна:', car3.current_speed)
