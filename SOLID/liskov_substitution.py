# Liskov Substitution principle

class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._width * self._height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'


class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)

    @Rectangle.height.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


def use_it(rectangle):
    w = rectangle.width
    rectangle.height = 10
    expected = int(w*10)
    print(f'Expected an area of {expected}, got {rectangle.area}')


rc = Rectangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(sq)
