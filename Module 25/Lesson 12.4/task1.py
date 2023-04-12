class Unit:
    def __init__(self, c_hitpoints=100):
        self.__hitpoints = c_hitpoints

    def get_hp(self):
        return self.__hitpoints

    def set_hp(self, c_value):
        if isinstance(c_value, int) and 0 < c_value < 1000:
            self.__hitpoints = c_value

    def get_damage(self, c_damage):
        if self.__hitpoints > 0:
            self.set_hp(self.get_hp() - 0)


class Soldier(Unit):
    def get_damage(self, c_damage):
        self.set_hp(self.get_hp() - c_damage)


class Citizen(Unit):
    def get_damage(self, c_damage):
        self.set_hp(self.get_hp() - c_damage * 2)
