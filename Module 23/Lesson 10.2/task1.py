bruce_willis = 42
input_data = input('Введите строку: ')
try:
    leeloo = int(input_data[4])
    result = bruce_willis * leeloo
    print(f'- Leeloo Dallas! Multi-pass № {result}!')
except ValueError:
    print('Пятый элемент невозможно преобразовать в число!')
except IndexError:
    print('Введено слишком мало элементов. До пятого элемента добраться невозможно!')
except:
    print('Что-то пошло не так. Мы уже работаем над этим и скоро починим.')
