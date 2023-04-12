from math import sqrt, ceil


class Primes:
    def __init__(self, c_max_value):
        self.__counter = 0
        self.__value = 0
        self.max_value = c_max_value

    def is_prime(self):
        if 0 <= self.__value <= 1:
            return False
        else:
            for m_divisor in range(2, ceil(sqrt(self.__value + 1))):
                if self.__value % m_divisor == 0:
                    return False
            else:
                return True

    def __iter__(self):
        self.__counter = 0
        self.__value = 0
        return self

    def __next__(self):
        if self.__counter <= self.max_value:
            while not self.is_prime():
                if self.__counter <= self.max_value:
                    self.__counter += 1
                    self.__value += 1
                else:
                    raise StopIteration
            else:
                m_return_value = self.__value
                self.__value += 1
                self.__counter += 1
                return m_return_value
        else:
            raise StopIteration


prime_nums = Primes(50)

for i_elem in prime_nums:
    print(i_elem, end=' ')
