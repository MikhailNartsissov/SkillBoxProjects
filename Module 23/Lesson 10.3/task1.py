string_to_write = input('Введите строку для записи в файл:')
destination_name = input('Введите имя файла, куда нужно записать строку:')
destination = None

try:
    destination = open(destination_name, 'w', encoding='utf-8')
    int(string_to_write)
except ValueError as exc:
    print(exc, 'Невозможно преобразовать данные в целое число.')
except FileNotFoundError:
    print('Файл с таким именем не найден.')
except NameError:
    print('Что-то пошло не так. Мы уже работаем над проблемой.')
else:
    destination.write(string_to_write)
finally:
    if destination is not None and not destination.closed:
        destination.close()
