class Human:
    __people = 0

    def __init__(self, c_name, c_age):
        self.__name = ''
        self.__age = 0
        self.set_name(c_name)
        self.set_age(c_age)
        Human.__people += 1

    @staticmethod
    def set_name(c_name):
        if isinstance(c_name, str) and c_name.isalpha():
            return c_name
        else:
            raise Exception('Имя должно состоять только из букв')

    @staticmethod
    def set_age(c_age):
        if isinstance(c_age, (int, float)) and 0 < c_age < 100:
            return c_age
        else:
            raise Exception('Возраст должен находиться в диапазоне от 0 до 100')

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
