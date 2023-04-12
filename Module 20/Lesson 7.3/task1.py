initial_string = input('Строка: ')

print('\nОтвет:', end=' ')
for symbol_index, symbol in enumerate(initial_string):
    if symbol == '~':
        print(symbol_index, end=' ')
