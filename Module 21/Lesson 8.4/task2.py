import re


def prepare_list(f_string):
    f_string = f_string[1:len(data) - 1]
    f_list = f_string.split(',')
    for f_item_index in range(len(f_list)):
        f_list[f_item_index] = f_list[f_item_index].strip()
    return f_list


def is_float(f_string):
    if re.match(r"\d+\.*\d*", f_string):
        return True
    else:
        return False


def data_type(f_string):
    if f_string.startswith('(') and f_string.endswith(')'):
        return 'кортеж', 'Неизменяемый (immutable)', tuple(prepare_list(f_string))
    elif f_string.startswith('[') and f_string.endswith(']'):
        return 'список', 'Изменяемый (mutable)', list(prepare_list(f_string))
    elif f_string.startswith('{') and f_string.endswith('}'):
        if ": " in f_string:
            prepared_data = prepare_list(f_string)
            for item_index in range(len(prepared_data)):
                prepared_data[item_index] = prepared_data[item_index].split(':')
            f_data = {prepared_data[index][0]: prepared_data[index][1] for index in range(len(prepared_data))}
            return 'словарь', 'Изменяемый (mutable)', f_data
        else:
            return 'множество', 'Изменяемый (mutable)', set(prepare_list(f_string))
    elif f_string.strip().isdecimal():
        return 'целое число', 'Неизменяемый (immutable)', int(f_string.strip())
    elif is_float(f_string.strip()):
        return 'вещественное число', 'Неизменяемый (immutable)', float(f_string.strip())
    elif f_string.strip().lower() == 'true' or f_string.strip().lower() == 'false':
        return 'логический', 'Неизменяемый (immutable)', bool(f_string.strip().capitalize())
    else:
        return 'строка', 'Неизменяемый (immutable)', f_string


data = input('Введите исходные данные: ')
type_of_data, changeable, data = data_type(data)
print('\nТип данных:', type_of_data)
print('Id объекта:', id(data))
