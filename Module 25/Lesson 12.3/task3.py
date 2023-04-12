class DivisionError(Exception):
    pass


def divide(f_number1, f_number2):
    if f_number1 >= f_number2:
        return f_number1 // f_number2
    else:
        raise DivisionError('Нельзя делить меньшее на большее!')


with open('numbers.txt', 'r', encoding='utf-8') as numbers:
    for line in numbers:
        elements = line.strip().split()
        try:
            result = divide(int(elements[0]), int(elements[1]))
        except DivisionError:
            result = divide(int(elements[1]), int(elements[0]))
        print(result)
