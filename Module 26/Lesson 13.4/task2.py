from random import random


class RandomIterator:
    def __init__(self, c_max_counter):
        self.__counter = 0
        self.__start_value = random()
        self.max_counter = c_max_counter

    def __iter__(self):
        self.__counter = 0
        self.__start_value = random()
        return self

    def __next__(self):
        if self.__counter <= self.max_counter:
            return_value = random() + self.__start_value
            self.__start_value = return_value
            self.__counter += 1
            return round(return_value, 2)
        else:
            raise StopIteration


print('\nЭлементы итератора:')
for i_element in RandomIterator(5):
    print(i_element)

print('\nЭлементы нового итератора:')
for i_element in RandomIterator(6):
    print(i_element)
