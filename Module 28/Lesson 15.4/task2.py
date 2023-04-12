from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, c_x: float = 0.0, c_y: float = 0.0, c_length: int = 1, c_width: int = 1) -> None:
        self.x = c_x
        self.y = c_y
        self.length = c_length
        self.width = c_width

    @abstractmethod
    def move(self, c_x: float = 0.0, c_y: float = 0.0) -> None:
        pass


class ResizableMixin(ABC):
    def __init__(self, c_length, c_width):
        super().__init__()
        self.length = c_length
        self.width = c_width

    def resize(self, c_length, c_width):
        self.length = c_length
        self.width = c_width


class Square(Figure, ResizableMixin):
    def __init__(self, c_x: float = 0.0, c_y: float = 0.0, c_size: int = 1) -> None:
        super().__init__(c_x, c_y, c_size, c_size)

    def move(self, c_x: float = 0.0, c_y: float = 0.0) -> None:
        self.x = c_x
        self.y = c_y


class Rectangle(Figure, ResizableMixin):
    def move(self, c_x: float = 0.0, c_y: float = 0.0) -> None:
        self.x = c_x
        self.y = c_y


square = Square(1, 1, 2)
rectangle = Rectangle(2, 2, 4, 8)

print(square.length, square.width)
print(rectangle.length, rectangle.width)
square.resize(5.4, 5.4)
rectangle.resize(6.7, 23.1)
print(square.length, square.width)
print(rectangle.length, rectangle.width)

print(square.x, square.y)
print(rectangle.x, rectangle.y)
square.move(15.4, 25.4)
rectangle.move(36.7, 73.1)
print(square.x, square.y)
print(rectangle.x, rectangle.y)
