initial_string = input('\nВведите строку: ')
initial_set = set(initial_string)
print('Различные цифры строки: ', end='')
for element in initial_set:
    if '0' <= element <= '9':
        print(element, end='')
