def caesar_cipher(f_text, f_shift):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
    f_encrypted_text = [alphabet[(alphabet.index(f_letter) + f_shift) % 33]
                        if f_letter != ' '
                        else ' '
                        for f_letter in f_text
                        ]
    return ''.join(f_encrypted_text)


original_text = input('\nВведите сообщение: ').lower()
shift = int(input('Введите сдвиг: '))

print('Зашифрованное сообщение: ', caesar_cipher(original_text, shift))
