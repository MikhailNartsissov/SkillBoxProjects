from typing import Callable, Any
from functools import wraps


def do_twice(f_function: Callable) -> Callable:
    """Декоратор, вызывающий дважды передаваемую в него функцию"""
    @wraps
    def wrapped_function(*args, **kwargs) -> Any:
        f_function(*args, **kwargs)
        return f_function(*args, **kwargs)
    return wrapped_function


@do_twice
def greeting(name: str) -> None:
    print('Привет, {name}!'.format(name=name))


greeting('Миша')
