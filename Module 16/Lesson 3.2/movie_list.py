def is_inl_ist(f_name, f_list):
    for f_item in f_list:
        if f_item == f_name:
            return True
    return False


films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня', 'Проклятый остров', 'Начало', 'Матрица']
top_movies = []
while True:
    print('\nВаш текущий топ фильмов:', top_movies)
    movie_to_add = input('Название фильма: ')
    if is_inl_ist(movie_to_add, films):
        print('Команды: добавить, вставить, удалить')
        action = input('Введите команду: ')
        if action == 'добавить':
            if is_inl_ist(movie_to_add, top_movies):
                print("Такой фильм уже есть в вашем топ-листе. Попробуйте ввести другой фильм.")
            else:
                top_movies.append(movie_to_add)
        if action == 'вставить':
            if is_inl_ist(movie_to_add, top_movies):
                print("Такой фильм уже есть в вашем топ-листе. Попробуйте ввести другой фильм.")
            else:
                position = int(input('На какое место вставить? '))
                top_movies.insert(position - 1, movie_to_add)
        if action == 'удалить':
            if not(is_inl_ist(movie_to_add, top_movies)):
                print("Такого фильма нет в вашем топ-листе. Попробуйте ввести другой фильм.")
            else:
                top_movies.remove(movie_to_add)
    else:
        print('Такого фильма нет в нашей коллекции. Попробуйте ввести другой фильм.')


