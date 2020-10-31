#Exercise 12-04
#Josh net182 201810701580043

from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self, colour):
        self.colour = colour

    def fill(self):
        print("Shape filled with {0}".format(self.colour))

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def draw(self):
        pass

class Rectangle(Shape):

    def __init__(self, colour, length, width):
        Shape.__init__(self, colour)
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def draw(self):
        print("Drawing a rectangle")

class Circle(Shape):

    def __init__(self, colour, radius):
        Shape.__init__(self, colour)
        self.radius = radius
    def get_area(self):
        return self.radius ** 2 * 3.14
    def draw(self):
        print('Drawing a circle')

shapes = [Circle("Blue", 10),Circle("White", 20),Rectangle("Black", 3, 5),Rectangle("Red", 7, 9)]

for i in shapes:
    i.fill()
    i.draw()

total_area = 0
max_area = shapes[0].get_area()
min_area = shapes[0].get_area()

for i in shapes:
    areal = i.get_area()
    total_area += areal
    if areal > max_area:
        max_area = areal
    if areal < min_area:
        min_area = areal

average_area = total_area/len(shapes)
print('{0:.2f}'.format(total_area))
print('{0:.2f}'.format(average_area))
print('{0:.2f}'.format(max_area))
print('{0:.2f}'.format(min_area))
