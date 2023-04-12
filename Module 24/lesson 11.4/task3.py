from random import randint


class Potato:
    degrees_of_maturity = {0: 'Не посажена', 1: 'Росток', 2: 'Зелёная', 3: 'Цветёт', 4: 'Созрела'}

    def __init__(self, c_bed_position=None, c_maturity=0):
        self.bed_position = c_bed_position
        self.maturity = c_maturity

    def grow(self):
        if self.maturity < 4:
            self.maturity += 1

    def maturity_degree(self):
        return self.maturity

    def is_grown(self):
        if self.maturity == 4:
            return True
        return False


class PotatoBed:

    def __init__(self, potato_amount=1):
        self.potatoes = [Potato(index) for index in range(1, potato_amount + 1)]

    def grow(self):
        for c_potato in self.potatoes:
            if c_potato.maturity < 4:
                c_potato.maturity += 1

    def is_grown(self):
        if all([i_potato.is_grown() for i_potato in self.potatoes]):
            print('Вся картошка созрела. Можно собирать!\n')
            return True
        else:
            print('Картошка ещё не созрела!\n')
            return False


potato_bed = PotatoBed(randint(1, 10))
print()
for i_index in range(5):

    if i_index == 0:
        print('Картошку предстоит посадить!')
    elif i_index == 1:
        print('Картошка прорастает!')
    elif i_index == 2:
        print('Картошка проросла, но не зацвела!')
    elif i_index == 3:
        print('Картошка зацвела!')
    elif i_index == 4:
        print('Картошка созрела!')

    for potato in potato_bed.potatoes:
        print('Картошка {} сейчас {}'.format(potato.bed_position, Potato.degrees_of_maturity[potato.maturity]))

    if not potato_bed.is_grown():
        potato_bed.grow()
