path = input('Путь к файлу: ')
disk = input('На каком диске должен лежать файл: ')
extension = input('Требуемое расширение файла: ')

if not path.startswith(disk):
    print('Ошибка: Имя диска указано неверно.')
elif not path.endswith(extension):
    print('Ошибка: Расширение файла указано неверно.')
else:
    print('Путь корректен!')
