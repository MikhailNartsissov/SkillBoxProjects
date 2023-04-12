source = None
total_sym = 0
length = 0
line_number = 0
try:
    source = open('names.txt', 'r', encoding='utf-8')
    for i_line in source:
        line_number += 1
        length = len(i_line)
        if i_line.endswith('\n'):
            length -= 1
        if length < 3:
            raise ValueError('В строке {} встречено имя короче трех символов'.format(line_number))
        total_sym += length
except ValueError:
    raise
else:
    print('Общее количество символов в именах:', total_sym)
finally:
    if source is not None and not source.closed:
        source.close()
