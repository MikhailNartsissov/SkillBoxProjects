from typing import Callable
from functools import wraps


global_count = {}


def counter(f_function: Callable) -> Callable:

    @wraps(f_function)
    def wrapper(*args, **kwargs) -> Callable:
        wrapper.count += 1
        global_count[f_function.__name__] = global_count.get(f_function.__name__, 0) + 1
        return f_function(*args, **kwargs)
    wrapper.count = 0
    return wrapper


@counter
def test():
    print('Вызвана тестовая функция')


@counter
def test2():
    print('Вызвана еще одна тестовая функция')


print(global_count, test.count, test2.count)
test()
test2()
print(global_count, test.count, test2.count)
test()
test2()
print(global_count, test.count, test2.count)
test()
test2()
print(global_count, test.count, test2.count)
