class EndlessIterator:
    def __init__(self):
        self.__counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        return_value = self.__counter
        self.__counter += 1
        return return_value


my_iter = EndlessIterator()
for i_elem in my_iter:
    print(i_elem)
