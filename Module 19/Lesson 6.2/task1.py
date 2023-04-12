small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}

big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}

big_storage.update(small_storage)
item_name = input('Введите название товара: ')
item_quantity = big_storage.get(item_name)
if item_quantity is None:
    print('Товара {0} на складе нет.'.format(item_name))
else:
    print('На складе {0} штук товара {1}.'.format(item_quantity, item_name))
