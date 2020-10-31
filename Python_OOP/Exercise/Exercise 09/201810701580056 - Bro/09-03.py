# exercise 09 03
'''
Bro
201810701580056
network 182
'''
class Shape:

    def __init__(self, colour):
        self.colour = colour

class Rectangle(Shape):

    def __init__(self, colour, height, width):
        Shape.__init__(self, colour)
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width


class Triangle(Shape):

    def __init__(self, colour, height,width):
        Shape.__init__(self, colour)
        self.height = height
        self.width = width

    def calculate_area(self):
        return  float(self.height * self.width * 0.5)


rec1 = Rectangle("red", 4, 5)
print(rec1.colour)
print(rec1.calculate_area())

tri1 = Triangle("blue", 6, 8)
print(tri1.colour)
print(tri1.calculate_area())

