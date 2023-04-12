words =[]
for i in range(3):
    print('Введите', i + 1, 'слово:', end=' ')
    words.append(input())
count = [0, 0, 0]

word = input('\nСлово из текста: ')
while word != 'end':
    for i in range(3):
        if word == words[i]:
            count[i] += 1
    word = input('Слово из текста: ')
print('\nПодсчет слов в тексте:')
for i in range(3):
    print(words[i], ': ', count[i], sep='')
