from typing import Callable
from functools import wraps


class HTTPServer:
    """
    Класс, имитирующий работу сервера,
    :arg c_function функция, формирующая ответ "сервера"

    """
    url = ''

    def __init__(self, c_function: Callable) -> None:
        self.function = c_function

    def get(self, m_url: str) -> Callable:
        """
        Метод, возвращающий функцию ответа. В данном случае это функция example, которая возвращается
        в случае, если адрес в запросе равен '//' или 'http://'.
        :param m_url: адрес запроса
        :return: функция ответа (example)
        """
        HTTPServer.url = m_url
        if m_url == '//' or m_url == 'http://':
            return self.function


def callback(f_url: str = '') -> Callable:
    """
    Декоратор, возвращающий ответ "сервера"
    :param f_url: адрес запроса
    :return: результат выполнения декорированной функции
    """
    def decorator(f_function: Callable) -> Callable:
        @wraps(f_function)
        def wrapper(*args, ** kwargs):
            if f_url == HTTPServer.url:
                return f_function(*args, **kwargs)
        return wrapper
    return decorator


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


# Основной код.
# Поскольку я не знаю, откуда был взят метод get для объекта app, я написал свой класс,
# который реализует нужные ответы "сервера".
# Экземпляр класса инициализируется функцией ответа. В данном случае это функция example,
# которую возвращает метод get в случае, если адрес в запросе равен '//' или 'http://'.
# На example навешен декоратор, выполняющий код функции только тогда, когда адрес равен '//'
# То есть в случае, если адрес в запросе равен '//', вернется:
# Пример функции, которая возвращает ответ сервера
# Ответ: OK
# Если адрес в запросе равен 'http://', вернется:
# Ответ: None
# Если в запросе указан любой другой адрес, вернется:
# 'Такого пути нет'.


app = HTTPServer(example)
route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
