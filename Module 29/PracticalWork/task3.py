from typing import Callable
from functools import wraps
from datetime import datetime
from time import time


def format_converter(f_format: str) -> str:
    """
    Функция преобразования строки-аргумента к строке формата даты и времени
    :param f_format: строка-аргумент, вида 'Y b d H:M:S'
    :return str:  строка формата, вида '%Y %b %d %H:%M:%S'
    """
    f_result = ''
    for letter in f_format:
        if letter.isalpha():
            letter = '%' + letter
        f_result += letter
    return f_result


def logging(cls, f_function: Callable, f_format: str = 'Y b d H:M:S') -> Callable:
    """
    Декоратор, выполняющий логирование запуска методов, определение родительского класса
    и подсчёт времени работы методов класса
    :param cls: класс, методы которого нужно декорировать
    :param f_function: декорируемый метод
    :param f_format: строка формата, вида 'Y b d H:M:S'
    :return: результат выполнения декорированной функции
    """
    @wraps(f_function)
    def wrapper(*args, **kwargs):
        print('Запускается \'{name}\'. Дата и время запуска {time}.'.format(
            name=cls.__name__ + '.' + f_function.__name__,
            time=datetime.now().strftime(format_converter(f_format))))
        f_start = time()
        f_result = f_function(*args, **kwargs)
        if cls.__bases__[0].__name__ == 'object':
            print('Тут метод {name}.'.format(
                name=f_function.__name__))
        else:
            print('Тут метод {name} у наследника.'.format(
                name=f_function.__name__))
        print('Завершение \'{name}\', время работы = {time} s.'.format(
            name=cls.__name__ + '.' + f_function.__name__,
            time=round(time() - f_start, 3)))
        return f_result
    return wrapper


def log_methods(f_format: str = 'Y b d H:M:S') -> Callable:
    """
    Декоратор, выполняющий декорирование всех методов класса, за исключением магических методов
    :param f_format: строка формата, вида 'Y b d H:M:S'
    :return: класс с декорированными методами (в качестве декоратора явно указан logging)
    """
    @wraps(logging)
    def decorate(cls):
        for f_method_name in dir(cls):
            if f_method_name.startswith('__') is False:
                f_method = getattr(cls, f_method_name)
                decorated_method = logging(cls, f_method, f_format)
                setattr(cls, f_method_name, decorated_method)
        return cls
    return decorate


@log_methods("b d Y — H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
