# Exercise 09-03
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''


class Shape:
    def __init__(self, colour):
        self.colour = colour


class Rectangle(Shape):

    def __init__(self, colour, width, height):
        Shape.__init__(self, colour)
        self.colour = colour
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Triangle(Shape):

    def __init__(self, colour, width, height):
        Shape.__init__(self, colour)
        self.colour = colour
        self.width = width
        self.height = height

    def calculate_area(self):
        return (self.width * self.height) / 2


rec1 = Rectangle('red', 4, 5)
print(rec1.colour)
print(rec1.calculate_area())

tri1 = Triangle('blue', 6, 8)
print(tri1.colour)
print(tri1.calculate_area())
