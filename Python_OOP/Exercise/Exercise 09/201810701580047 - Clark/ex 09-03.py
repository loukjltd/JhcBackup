# Exercise 09-03
'''
name:Clark
class:net182
I  D:201810701580047
'''
class Shape:
    def __init__(self, colour):
        self.__colour = colour

    def colour(self):
        print(self.__colour)


class Rectangle(Shape):
    def __init__(self, colour, width, height):
        Shape.__init__(self, colour)
        self.__width = width
        self.__height = height
        self.__area = width * height

    def calculate_area(self):
        print('%.1f' % self.__area)


class Triangle(Shape):
    def __init__(self, colour, width, height):
        Shape.__init__(self, colour)
        self.__width = width
        self.__height = height
        self.__area = width * height

    def calculate_area(self):
        print('%.1f' % self.__area)


rec1 = Rectangle("red", 4, 5)
rec1.colour()
rec1.calculate_area()

tri1 = Triangle("blue", 6, 8)
tri1.colour()
tri1.calculate_area()
