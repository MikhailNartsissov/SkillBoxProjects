class Robot:
    def __init__(self, c_model):
        self.model = c_model

    def operate(self):
        print('Робот выполняет свою работу.')


class VacuumCleaner(Robot):
    def __init__(self, c_model, c_dust_container=0):
        super().__init__(c_model)
        self.dust_container = c_dust_container

    def operate(self):
        self.dust_container += 1
        print('Робот {} пылесосит пол. Текущая заполненность контейнера составляет {}'.
              format(self.model, self.dust_container))


class MilitaryRobot(Robot):
    def __init__(self, c_model, c_weapon):
        super().__init__(c_model)
        self.weapon = c_weapon

    def operate(self):
        print('Робот {} защищает военный объект. Используемое оружие: {}'.format(self.model, self.weapon))


class SubmarineRobot(MilitaryRobot):
    def __init__(self, c_model, c_weapon, c_depth):
        super().__init__(c_model, c_weapon)
        self.depth = c_depth

    def operate(self):
        print('Робот {} защищает военный объект под водой на глубине {}. Используемое оружие: {}'.
              format(self.model, self.depth, self.weapon))


cleaner = VacuumCleaner('SuperCleaner 2.232', 3)
cleaner.operate()
warrior = MilitaryRobot('Predator 414C', 'миномёт')
warrior.operate()
submarine = SubmarineRobot('RedOctober1989', 'ядерные ракеты', '400 метров')
submarine.operate()
