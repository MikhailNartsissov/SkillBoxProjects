from math import sqrt, ceil


def endless_prime_values(f_start_value):
    while True:
        if f_start_value > 1:
            for m_divisor in range(2, ceil(sqrt(f_start_value + 1))):
                if f_start_value % m_divisor == 0:
                    break
            else:
                yield f_start_value
        f_start_value += 1


for value in endless_prime_values(0):
    print(value)
