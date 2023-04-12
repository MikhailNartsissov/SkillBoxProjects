def special_symbols(f_list):
    f_special_symbols = 0
    for f_symbol in f_list:
        if f_symbol == '!' or f_symbol == '?':
            f_special_symbols += 1
    return f_special_symbols


first_message = list(input('Первое сообщение: '))
second_message = list(input('Второе сообщение: '))

if special_symbols(first_message) > special_symbols(second_message):
    if not(len(second_message) == special_symbols(second_message)):
        second_message.insert(0, ' ')
    first_message.extend(second_message)
    for letter in first_message:
        print(letter, end='')
elif special_symbols(first_message) == special_symbols(second_message):
    print('Ой!')
else:
    if not(len(first_message) == special_symbols(first_message)):
        first_message.insert(0, ' ')
    second_message.extend(first_message)
    for letter in second_message:
        print(letter, end='')
