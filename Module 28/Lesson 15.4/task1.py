from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, c_color: str = 'white', c_speed: float = 0.0, c_distance: float = 0.0) -> None:
        self.color = c_color
        self.speed = c_speed
        self.distance = c_distance

    @abstractmethod
    def move(self, c_speed):
        pass

    @abstractmethod
    def beep(self):
        pass


class Car(Transport):

    def move(self, c_speed):
        self.speed = c_speed
        self.distance += self.speed

    def beep(self):
        print('beep!')


class Boat(Transport):

    def sail(self, c_speed):
        print('Поднять паруса!')
        self.speed = c_speed
        self.distance += self.speed

    def move(self, c_speed):
        pass

    def beep(self):
        print('Bop!')


class CanPlayMusicMixin:
    def play_music(self):
        print("""If you’re drifting on an empty ocean
        With no wind to fill your sail
        The future, your horizon
        It’s like searching for the Holy Grail...""")


class Amphibian(Car, Boat, CanPlayMusicMixin):
    pass


car = Car()
boat = Boat()
amphibian = Amphibian()

amphibian.move(100)
amphibian.play_music()
amphibian.sail(50)
print(amphibian.distance)
