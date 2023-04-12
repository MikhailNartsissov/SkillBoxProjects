from typing import Callable


def func_2(f_function: Callable, *args, **kwargs) -> int:
    return f_function(*args, **kwargs) * f_function(*args, **kwargs)


def func_1(x: int) -> int:
    return x + 10


print(func_2(func_1, 9))
