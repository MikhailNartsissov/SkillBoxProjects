from random import randint


class Point:
    total_points = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Point.total_points += 1

    def show_point(self):
        print('Координата Х: {}\nКоордината Y: {}\n'.format(self.x, self.y))


points = [Point(randint(0, 200), randint(0, 200)) for _ in range(randint(1, 10))]
print(Point.total_points)
for index in range(Point.total_points):
    points[index].show_point()
