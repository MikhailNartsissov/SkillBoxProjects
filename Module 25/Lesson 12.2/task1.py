class Point:
    count = 0

    def __init__(self, c_x=0, c_y=0):
        self.__x = c_x
        self.__y = c_y
        Point.count += 1

    def __str__(self):
        return 'Точка с координатами {}, {}'.format(self.__x, self.__y)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    @staticmethod
    def check_value(c_value):
        if isinstance(c_value, str) and c_value.isdigit():
            c_value = float(c_value)
        if isinstance(c_value, (float, int)):
            return c_value
        return None

    def set_x(self, c_x):
        c_checked_x = self.check_value(c_x)
        if c_checked_x:
            self.__x = c_checked_x

    def set_y(self, c_y):
        c_checked_y = self.check_value(c_y)
        if c_checked_y:
            self.__y = c_checked_y

    def show_point(self):
        print('Координата Х: {}\nКоордината Y: {}\n'.format(self.__x, self.__y))
