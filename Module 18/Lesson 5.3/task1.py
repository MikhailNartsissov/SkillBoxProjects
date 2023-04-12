words = input('Введите слова для подсчета через запятую: ').split(', ')
text = input('Введите текст произведения: ').split()
words_count = [text.count(word) for word in words]

for i in range(len(words)):
    output_template = 'Слово {word} встречается во введенном тексте {words_count} раз.'.format(
        word=words[i],
        words_count=words_count[i]
    )
    print(output_template)
