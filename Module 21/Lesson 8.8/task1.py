def pr_num(f_num):
    if not isinstance(f_num, int) or f_num < 1:
        print('Ошибка:')
        print('Функция pr_num() в качестве параметра может принимать только целые числа больше 0.')
        return
    if f_num == 1:
        print(f_num)
    else:
        pr_num(f_num - 1)
        print(f_num)

# print для проверки
# pr_num(10)
# pr_num(-1)
# pr_num(0)
# pr_num(1.234)
