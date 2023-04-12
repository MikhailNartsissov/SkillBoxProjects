from typing import Callable, Any


def decorator(f_function: Callable) -> Callable:
    """Декоратор, вызывающий дважды передаваемую в него функцию"""
    def wrapped_function(*args, **kwargs) -> Any:
        f_function(*args, **kwargs)
        return f_function(*args, **kwargs)
    return wrapped_function


@decorator
def greeting(name: str) -> None:
    print('Привет, {name}!'.format(name=name))


greeting('Миша')
