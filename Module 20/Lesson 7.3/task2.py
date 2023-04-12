from random import choice


alphabet = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
first_list = [choice(alphabet) for _ in range(10)]
second_list = [choice(alphabet) for _ in range(10)]
first_dict = {element_index: element_value for element_index, element_value in enumerate(first_list)}
second_dict = {element_index: element_value for element_index, element_value in enumerate(second_list)}

print('\nПервый список:', first_list)
print('Второй список:', second_list)
print('\nПервый словарь:', first_dict)
print('Второй словарь:', second_dict)
