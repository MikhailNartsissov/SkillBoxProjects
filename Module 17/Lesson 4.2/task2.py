initial_text = input('Введите строку: ')
symbol_to_add = input('Введите дополнительный символ: ')

print('\nСписок удвоенных символов:', [element * 2 for element in initial_text])
print('Склейка с дополнительным символом:', [element * 2 + symbol_to_add for element in initial_text])
