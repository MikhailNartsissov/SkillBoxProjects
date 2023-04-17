from typing import Callable, Any
from functools import wraps


def repeat(_function=None, *, f_repeats: int = 2) -> Callable:
    def do_any(f_function: Callable) -> Callable:
        """Декоратор, вызывающий дважды передаваемую в него функцию"""
        @wraps(f_function)
        def wrapped_function(*args, **kwargs) -> Any:
            for f_counter in range(f_repeats - 1):
                f_function(*args, **kwargs)
            return f_function(*args, **kwargs)
        return wrapped_function
    if _function is None:
        return do_any
    return do_any(_function)


@repeat(f_repeats=15)
def greeting(name: str) -> None:
    print('Привет, {name}!'.format(name=name))


greeting('Миша')
