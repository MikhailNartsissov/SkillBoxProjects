class Example:
    def __init__(self) -> None:
        print('Вызов __init__')

    def __enter__(self) -> bool:
        print('Вызов __enter__')
        return True

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        print('Вызов __exit__')
        if exc_type:
            print('Тип ошибки: {exc_type}\nЗначение ошибки: {exc_val}\n"След" ошибки: {exc_tb}'.
                  format(exc_type=exc_type, exc_val=exc_val, exc_tb=exc_tb))
            return True


my_obj = Example()
with my_obj as obj:
    print('Код внутри первого вызова контекст менеджера')
    with my_obj as obj2:
        raise Exception('Выброс исключения во вложенном (втором) вызове контекст менеджере')
    print('Я обязательно выведусь...')
