goods = [["яблоки", 50.0], ["апельсины", 190.0], ["груши", 100.0], ["нектарины", 200.0], ["бананы", 77.0]]
print('Текущий ассортимент: ', goods)
fruit_name = input('Новый фрукт: ')
price = round(float(input('Цена: ')), 2)
goods.append([fruit_name, price])
print('Новый ассортимент: ', goods)
for good in goods:
    good[1] = round(good[1] * 1.08, 2)
print('Новый ассортимент с увеличенной ценой: ', goods)
