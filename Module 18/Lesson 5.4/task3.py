initial_string = input('Введите строку: ')
lower = 0
upper = 0
for letter in initial_string:
    if letter.islower():
        lower += 1
    else:
        upper += 1
if lower > upper:
    print(initial_string.lower())
else:
    print(initial_string.upper())
