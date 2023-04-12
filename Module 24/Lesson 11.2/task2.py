class Monitor:
    name = 'Samsung'
    matrix = 'VA'
    res = 'WQHD'
    freq = 60


class Headphones:
    name = 'Sony'
    sensitivity = 108
    micro = True


monitors = [Monitor() for _ in range(4)]
headphones = [Headphones() for _ in range(3)]

for index, number in enumerate([60, 144, 70, 60]):
    monitors[index].freq = number

headphones[0].micro = False
