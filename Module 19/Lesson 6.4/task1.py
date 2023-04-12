punctuation_symbols = set(".,;:!?")
initial_string = input('Введите строку: ')
punctuation_in_string = set(
    [letter
     for letter in initial_string
     if letter in punctuation_symbols
     ]
)
print('\nКоличество знаков пунктуации:', len(punctuation_in_string))
