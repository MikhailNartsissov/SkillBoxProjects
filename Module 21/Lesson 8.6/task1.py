def ask_user(f_question,
             f_err_msg='Некорректный вводЮ пожалуйста, введите да или нет.',
             f_retries=3):
    while f_retries > 0:
        f_answer = input(f_question).strip().lower()
        if f_answer == 'да':
            return True
        elif f_answer == 'нет':
            return False
        else:
            f_retries -= 1
            print(f_err_msg)
            print('Осталось попыток:', f_retries)
    print('Превышено максимально допустимое число попыток. Работа прекращена.')
    return None


ask_user('Вы действительно хотите выйти (да/нет)? ')
ask_user('Записать файл (да/нет)? ', f_err_msg='Так записать или нет?')
ask_user('Удалить файл (да/нет)? ', f_err_msg='Не понял. Еще раз, пожалуйста.', f_retries=5)
ask_user('Продолжить работу (да/нет)? ', f_retries=4)
