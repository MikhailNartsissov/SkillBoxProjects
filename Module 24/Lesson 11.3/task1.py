class Toyota:

    def __init__(self, c_color='Red', c_price=1000000, c_max_speed=200, c_current_speed=0):
        self.color = c_color
        self.price = c_price
        self.max_speed = c_max_speed
        self.current_speed = c_current_speed

    def show_info(self):
        print('\nЦвет автомобиля: {}\nСтоимость автомобиля: '
              '{}\nМаксимальная скорость: {}\nТекущая скорость: {}\n'.format(self.color,
                                                                             self.price, self.max_speed,
                                                                             self.current_speed))

    def set_speed(self, c_speed):
        self.current_speed = c_speed


cars = [Toyota(color) for index, color in enumerate(['зелёный', 'красный', 'синий'])]
for index in range(3):
    cars[index].show_info()
