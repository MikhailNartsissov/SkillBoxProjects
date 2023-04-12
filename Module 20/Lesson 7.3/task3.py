def prepare_list(f_string):
    f_string = f_string[1:len(data) - 1]
    f_list = f_string.split(',')
    for f_item_index in range(len(f_list)):
        f_list[f_item_index] = f_list[f_item_index].strip()
    return f_list


data = input('Введите исходные данные: ')
if data.startswith('(') and data.endswith(')'):
    print('Элементы кортежа с чётным индексом:', end=' ')
    data = tuple(prepare_list(data))
elif data.startswith('[') and data.endswith(']'):
    print('Элементы списка с чётным индексом:', end=' ')
    data = list(prepare_list(data))
elif data.startswith('{') and data.endswith('}'):
    if ": " in data:
        print('Элементы словаря с чётным индексом:', end=' ')
        prepared_data = prepare_list(data)
        for item_index in range(len(prepared_data)):
            prepared_data[item_index] = prepared_data[item_index].split(':')
        data = {prepared_data[index][0]: prepared_data[index][1] for index in range(len(prepared_data))}
    else:
        print('Элементы множества с чётным индексом:', end=' ')
        data = set(prepare_list(data))
else:
    print('Символы строки с чётным индексом:', end=' ')


if isinstance(data, tuple):
    print('(', end='')
elif isinstance(data, list) or isinstance(data, str):
    print('[', end='')
elif isinstance(data, dict) or isinstance(data, set):
    print('{', end='')

for element_index, element_value in enumerate(data):
    if element_index % 2 == 0:
        if isinstance(data, dict):
            if element_index == 0:
                print(element_value, ':', data[element_value], sep='', end='')
            else:
                print(', ', element_value, ':', data[element_value], sep='', end='')
        elif isinstance(data, str):
            if element_index == 0:
                print('\'', element_value, '\'',  sep='', end='')
            else:
                print(', \'', element_value, '\'', sep='', end='')
        else:
            if element_index == 0:
                print(element_value, sep='', end='')
            else:
                print(', ', element_value, sep='', end='')

if isinstance(data, tuple):
    print(')', end='')
elif isinstance(data, list) or isinstance(data, str):
    print(']', end='')
elif isinstance(data, dict) or isinstance(data, set):
    print('}', end='')
print()
