import os


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
file_find(pathname, filename)
output_file = open('scripts.txt', 'a', encoding='utf-8')
for i_file in filelist:
    file_to_add = open(i_file, 'r', encoding='utf-8')
    for i_line in file_to_add:
        output_file.write(i_line)
    output_file.write('\n' + '*' * 80 + '\n' * 2)
    file_to_add.close()
output_file.close()
