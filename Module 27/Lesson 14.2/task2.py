from typing import Callable, Any
from time import time


def timer(f_function: Callable, *args: Any, **kwargs: Any) -> Any:
    f_start = time()
    f_function(*args, **kwargs)
    f_end = time()
    return round(f_end - f_start, 4)


def heavy_function(f_number: int) -> int:
    for _ in range(100000):
        f_number += f_number ** 3 / 10000000
    return f_number


print(timer(heavy_function, 3))
