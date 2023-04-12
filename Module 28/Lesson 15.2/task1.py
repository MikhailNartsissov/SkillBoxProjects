class Robot:
    """Робот - имеет модель и может вывести сообщение «Я — Робот». """
    def ___init___(self, f_model: str) -> None:
        self.model = f_model

    @staticmethod
    def intro() -> None:
        """Метод для вывода сообщения Я - робот!"""
        print('Я-робот!')


class CanFly:
    """
    Объекты этого класса умеют летать, дополнительно имеют атрибуты «Высота» и «Скорость»,
     а также может взлетать, летать и приземляться.
    """
    def __init__(self, c_height: int = 0, c_speed: int = 0) -> None:
        self.height = c_height
        self.speed = c_speed

    def takeoff(self) -> None:
        self.height = 1000
        self.speed = 300

    def fly(self) -> None:
        self.speed += 100

    def landing(self) -> None:
        self.speed = 0
        self.height = 0


class ReconDrone(Robot, CanFly):
    """Разведывательный дрон просто летает в поиске противника. При команде operate он выводит
    сообщение «Веду разведку с воздуха» и передвигается немного вперёд. """
    def __init__(self, c_position: int = 0) -> None:
        super().__init__()
        self.position = c_position

    def operate(self) -> None:
        self.position += 1
        print('Веду разведку с воздуха')


class FMR(Robot, CanFly):
    """ У летающего военного робота есть оружие, и при команде operate он выводит сообщение
     о защите военного объекта с воздуха с помощью этого оружия."""
    def __init__(self, c_position: int = 0, c_weapon: str = 'ракет') -> None:
        super().__init__()
        self.position = c_position
        self.weapon = c_weapon

    def operate(self) -> None:
        self.position += 1
        print('Защищаю военный объект с помощью {weapon}'.format(weapon=self.weapon))


fmr = FMR(c_weapon='самонаводящихся ракет')
rd = ReconDrone()

fmr.intro()
rd.intro()
fmr.takeoff()
rd.takeoff()
print(fmr.speed, fmr.height)
rd.fly()
print(rd.speed, rd.height)
rd.operate()
fmr.operate()
