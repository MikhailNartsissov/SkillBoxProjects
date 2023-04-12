def price_with_percent(f_price, f_percent):
    return round(f_price * (1 + f_percent / 100), 2)


initial_price = [round(float(input('Цена на товар: ')), 2) for _ in range(5)]
first_year = int(input('Повышение на первый год: '))
second_year = int(input('Повышение на второй год: '))
first_year_price = [price_with_percent(price, first_year) for price in initial_price]
second_year_price = [price_with_percent(price, second_year) for price in first_year_price]
print('Сумма цен за каждый год: ', round(sum(initial_price), 2), round(sum(first_year_price), 2),
      round(sum(second_year_price), 2))
