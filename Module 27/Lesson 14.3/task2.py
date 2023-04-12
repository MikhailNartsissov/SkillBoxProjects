from time import time
from typing import Callable, Any


def timer(f_function: Callable) -> Callable:
    """Декоратор для замера времени выполнения передаваемой функции"""
    def wrapped_function(*args, **kwargs) -> Any:
        f_start = time()
        f_result = f_function(*args, **kwargs)
        f_stop = time()
        print('Время выполнения функции составило {} секунд'.format(f_stop - f_start))
        return f_result
    return wrapped_function


@timer
def cubes(f_number: int) -> int:
    for _ in range(10):
        f_number += f_number ** 3
    return f_number


print(cubes(30))
