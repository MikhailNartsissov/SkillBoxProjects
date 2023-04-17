from re import match, search, findall, sub, compile

text = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'
t_pattern = compile(r'wo')
print('\nПоиск шаблона "wo"в начале строки:', match(t_pattern, text))
result = search(t_pattern, text)
print('Поиск первого найденного совпадения по шаблону "wo":', result)
print('Содержимое найденной подстроки: ', result.group())
print('Начальная позиция:', result.start())
print('Конечная позиция:', result.end())
print('Список всех упоминаний шаблона:', findall(t_pattern, text))
print('Текст после замены:', sub(t_pattern, 'ЗАМЕНА', text))
