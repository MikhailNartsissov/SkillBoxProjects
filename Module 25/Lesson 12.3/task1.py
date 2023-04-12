class Ship:
    def __init__(self, c_model):
        self.model = c_model

    def __str__(self):
        return 'Корабль модели', self.model

    def go(self):
        print('Корабль {} отправился в плавание'.format(self.model))


class CargoShip(Ship):
    def __init__(self, c_model, c_payload, c_cargo=0):
        super().__init__(c_model)
        self.payload = c_payload
        self.cargo = c_cargo

    def load(self, c_weight):
        if self.cargo + c_weight <= self.payload:
            self.cargo += c_weight
        else:
            raise Exception('Перегруз!')

    def unload(self, c_weight):
        if self.cargo >= c_weight:
            self.cargo -= c_weight
        else:
            raise Exception('Недостача груза!')


class WarShip(Ship):
    def __init__(self, c_model, c_weapon):
        super().__init__(c_model)
        self.model = c_model
        self.weapon = c_weapon

    def attack(self):
        print('Корабль {} атакует противника. Используемое оружие: {}.'.format(self.model, self.weapon))


cargo_ship = CargoShip('Академик Иванов', 20000000)
war_ship = WarShip('Стремительный', 'баллистические ракеты')

print(cargo_ship.__str__())
print(war_ship.__str__())
cargo_ship.go()
cargo_ship.load(40000)
print(cargo_ship.cargo)
cargo_ship.unload(2000)
print(cargo_ship.cargo)
war_ship.go()
war_ship.attack()
