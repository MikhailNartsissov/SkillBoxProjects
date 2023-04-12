initial_text = input('Введите текст: ')
letter_dict = dict()
for letter in initial_text:
    if letter in letter_dict:
        letter_dict[letter] += 1
    else:
        letter_dict[letter] = 1
for letter in sorted(letter_dict.keys()):
    print(letter, ':', letter_dict[letter])
print('Максимальная частота: ', max(letter_dict.values()))
