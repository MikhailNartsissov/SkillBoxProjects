from datetime import datetime


def is_palindrome(f_string):
    f_dict = dict()
    if f_string.endswith('\n'):
        f_string = f_string[:- 1]
    for f_letter in f_string:
        if f_letter.isdigit():
            raise ValueError('В строке обнаружена цифра!')
        if f_letter in f_dict:
            f_dict[f_letter] += 1
        else:
            f_dict[f_letter] = 1
    return palindrome_check(f_dict)


def palindrome_check(f_dict):
    f_counter = 0
    for f_item in f_dict:
        if f_dict[f_item] % 2 != 0:
            f_counter += 1
            if f_counter > 1:
                return False
    return True


source = None
destination = None
palindromes = 0
line_number = 0
try:
    source = open('words.txt', 'r', encoding='utf-8')
    for i_line in source:
        line_number += 1
        if is_palindrome(i_line):
            palindromes += 1
    print('Количество слов, из которых можно получить палиндром:', palindromes)
except ValueError:
    destination = open('errors.log', 'a', encoding='utf-8')
    destination.write(str(datetime.now()) + ' ' +
                      'В строке {} обнаружено число.\n'.format(line_number))
    raise
finally:
    if source is not None and not source.closed:
        source.close()
    if destination is not None and not destination.closed:
        destination.close()
