import os
from random import randint


def file_find(f_path, f_name):
    for f_element in os.listdir(f_path):
        c_path = os.path.join(f_path, f_element)
        if f_name == f_element:
            filelist.append(c_path)
        if os.path.isdir(c_path):
            file_find(c_path, f_name)
    else:
        return None


pathname = input('Ищем в: ')
filename = input('Имя файла: ')
filelist = list()
print('Найдены следующие пути: ')
file_find(pathname, filename)
print(filelist)
random_file = open(
    filelist[
        randint(0, len(filelist)
                )
    ],
    'r',
    encoding='utf-8'
)
for i_line in random_file:
    print(i_line)
random_file.close()
