from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, color: str = 'white', speed: float = 0.0, distance: float = 0.0) -> None:
        self._color = color
        self._speed = speed
        self._distance = distance

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, color: str) -> None:
        if color in ['white', 'yellow', 'green', 'red', 'orange', 'blue', 'violet', 'black', 'cyan', 'magenta']:
            self._color = color
        else:
            raise ValueError('Недопустимое значение цвета!')

    @property
    def speed(self) -> float:
        return self._speed

    @speed.setter
    def speed(self, speed: float) -> None:
        if speed >= 0:
            self._speed = speed
        else:
            raise ValueError('Недопустимое значение скорости!')

    @property
    def distance(self) -> float:
        return self._distance

    @distance.setter
    def distance(self, distance: float) -> None:
        if distance >= 0:
            self._distance = distance
        else:
            raise ValueError('Недопустимое значение пройденного расстояния!')

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
    @classmethod
    def play_music(cls):
        print("""If you’re drifting on an empty ocean
        With no wind to fill your sail
        The future, your horizon
        It’s like searching for the Holy Grail...""")


class Amphibian(Car, Boat, CanPlayMusicMixin):
    pass


car = Car(color='red')
boat = Boat(color='blue')
amphibian = Amphibian(color='beer')
print(boat.distance)
print(car.color)
print(amphibian.speed)
boat.distance = 12.3
amphibian.distance = 123.123
car.color = 'yellow'
amphibian.speed = 25.12
print(boat.distance)
print(car.color)
print(amphibian.speed)

amphibian.move(100)
amphibian.play_music()
amphibian.sail(50)
print(amphibian.distance)
