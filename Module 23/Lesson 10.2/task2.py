age_names = {10: 'Детство', 20: 'Нежный возраст', 30: 'Юность', 40: 'Молодость', 50: 'Взрослость', 60: 'Зрелость',
             70: 'Вторая зрелость', 80: 'Мудрость', 90: 'Солидный возраст', 100: 'Суперэйджер'}
try:
    source = open('ages.txt', 'r', encoding='utf-8')
    destination = open('result.txt', 'x', encoding='utf-8')
    for i_line in source:
        for i_key, i_value in age_names.items():
            if i_key == int(i_line.strip()):
                destination.write(i_line.strip() + ' - ' + i_value + '\n')
    source.close()
    destination.close()
except FileExistsError:
    print('Файл с именем result.txt уже существует.')
except FileNotFoundError:
    print('Файл с именем ages.txt не существует или не найден.')
except (TypeError, ValueError):
    print('Такие данные обработать невозможно. Проверьте тип данных или значения.')
