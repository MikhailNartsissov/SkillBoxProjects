from typing import Callable
from functools import wraps


def check_permission(user_id: str = None) -> Callable:
    """
    Декоратор проверяет, есть ли у пользователя доступ к вызываемой функции,
    и если нет, то выдаёт исключение PermissionError

    :param user_id: идентификатор пользователя
    :return decorator: результат выполнения декорированной функции
    """
    def decorator(f_function: Callable) -> Callable:
        @wraps(f_function)
        def wrapper(*args, **kwargs):
            with open('permissions.txt', 'r', encoding='utf-8') as permissions:
                for line in permissions:
                    if user_id in line.strip().split(';'):
                        if f_function.__name__ in line.strip().split(';'):
                            return f_function(*args, **kwargs)
                        else:
                            raise PermissionError('у пользователя {user} недостаточно прав,'
                                                  ' чтобы выполнить функцию {func}'.format(user=user_id,
                                                                                           func=f_function.__name__))
        return wrapper
    return decorator


# Проверочный код
@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
