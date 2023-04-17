from functools import wraps
from datetime import datetime
from time import sleep


def create_time(cls):
    """
    Декоратор класса. Выдаёт дату и время создания, а также список всех методов объекта
    класса каждый раз, когда объект класса создаётся в основном коде.
    :param cls:
    :return:
    """
    @wraps(cls)
    def wrapper(*args, **kwargs) -> cls:
        f_instance = cls(*args, **kwargs)
        print('\nНовый экземпляр класса создан:', datetime.now())
        print('Методы класса: ', end='')
        for f_method in dir(cls):
            if f_method.startswith('__') is False:
                print(f_method, end='; ')
        return f_instance
    return wrapper


@create_time
class Dog:
    def __init__(self, c_name: str, c_weight: int = 10) -> None:
        self.name = c_name
        self.weight = c_weight

    def get_name(self) -> str:
        return self.name

    def feed(self, c_amount):
        self.weight += c_amount


my_dog = Dog('Даша', 25)
sleep(2)
your_dog = Dog('Бобик', 30)
