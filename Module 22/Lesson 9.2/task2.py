import os


def file_find(f_path, f_name):
    for f_element in os.listdir(f_path):
        c_path = os.path.join(f_path, f_element)
        if f_name == f_element:
            print(c_path)
        if os.path.isdir(c_path):
            file_find(c_path, f_name)
    else:
        return None


pathname = input('Ищем в: ')
filename = input('Имя файла: ')
print('Найдены следующие пути: ')
file_find(pathname, filename)
