from re import findall

text = 'How much \wwood+?, would a \wwood+?chuck \dwwood+, chuck if a \wwood+?,chuck could chuck \wwood?,'
print('Список всех упоминаний шаблона:', findall(r'\\wwood\+\?,', text))
