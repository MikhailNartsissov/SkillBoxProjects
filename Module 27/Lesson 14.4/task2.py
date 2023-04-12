from typing import Callable, Dict


PLUGINS: Dict[str, Callable] = dict()


def reg_as_plugin(f_function: Callable) -> Callable:
    """Декоратор для помещения функции в словарь плагинов
    :type f_function: Callable
    """
    PLUGINS[f_function.__name__] = f_function
    return f_function


@reg_as_plugin
def filling(f_filling: str) -> None:
    print(f_filling)


filling('Soy meat')
print(PLUGINS)
