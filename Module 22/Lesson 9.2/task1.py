import os


path = input('Путь:')

if os.path.exists(path):
    if os.path.isdir(path):
        print('Это директория.')
    elif os.path.isfile(path):
        print('Это файл.')
        print('Размер файла:', os.path.getsize(path), 'байт')
    elif os.path.islink(path):
        print('Это ссылка.')
else:
    print('Указанного пути не существует.')
