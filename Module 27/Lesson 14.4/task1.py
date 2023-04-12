from typing import Callable, Any


def bread(f_function: Callable) -> Callable:
    """Декоратор для помещения начинки и ингредиентов между булочками"""
    def wrapped_function(*args, **kwargs) -> Any:
        print('\n</----------\>')
        f_result = f_function(*args, **kwargs)
        print('<\______/>')
        return f_result
    return wrapped_function


def ingredients(f_function: Callable) -> Callable:
    """Декоратор для помещения начинки между ингредиентами"""
    def wrapped_function(*args, **kwargs) -> Any:
        print('#помидоры#')
        f_result = f_function(*args, **kwargs)
        print('~салат~')
        return f_result
    return wrapped_function


@bread
@ingredients
def filling() -> None:
    print('--ветчина--')


filling()
