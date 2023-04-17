from typing import Callable, Any
from functools import wraps
from time import sleep


def universal_moderator(_function=None, *, f_delay: float = 5.0) -> Callable:
    def moderator(f_function: Callable) -> Callable:
        """Декоратор, задерживающий начало выполнения переданной в него функции на 5 секунд."""
        @wraps(f_function)
        def wrapped_function(*args, **kwargs) -> Any:
            sleep(f_delay)
            return f_function(*args, **kwargs)
        return wrapped_function
    if _function is None:
        return moderator
    return moderator(_function)


@universal_moderator(f_delay=15.0)
def say_something(what: str, to_whom: str = 'somebody') -> str:
    """Проверочная функция.
    :args: Один позиционный аргумент.
    :kwargs: один именованный аргумент
    :return: строка из двух аргументов

    С декоратором moderate исполнение начинается через f_delay секунд после запуска
    """
    return '\n{what}, {to_whom}.'.format(what=what, to_whom=to_whom)


print(say_something('Привет', 'дорогой друг'))

# Проверяем wraps()
print(say_something.__doc__)
