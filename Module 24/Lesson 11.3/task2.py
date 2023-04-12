class Family:
    name = 'Common family'
    funds = 100000
    is_house = False

    def show_info(self):
        print('\nНазвание семьи: {}\nТекущий баланс средств: {}\nДом '
              'куплен: {}\n'.format(self.name, self.funds, self.is_house))

    def earn_money(self, incomes):
        self.funds += incomes
        return self.funds

    def buy_house(self, price, discount=0):
        if self.funds >= round(price - price * discount / 100, 2):
            self.funds -= round(price - price * discount / 100, 2)
            self.is_house = True
            return True
        else:
            return False


def try_buy(f_family, f_price, f_discount):
    if f_family.buy_house(20000000, 5):
        print('Ура! Дом куплен за ',  '{0:,}'.format(round(f_price -
                                                           f_price * f_discount / 100, 2)).replace(',', ' '),
              'рублей')
        print('У семьи осталось {0:,} рублей'.format(f_family.funds).replace(',', ' '))
    else:
        print('Денег нет, но вы держитесь там!\n')


family = Family()
family.show_info()
print('Пытаемся купить дом за 20 000 000 рублей. Нам обещали скидку 5%.')
try_buy(family, 20000000, 5)
print('Ура! Удалось накопить 19 900 000 рублей\n')
family.earn_money(19900000)
print('Снова пытаемся купить дом за 20 000 000 рублей. Нам опять обещали скидку 5%.')
try_buy(family, 20000000, 5)
