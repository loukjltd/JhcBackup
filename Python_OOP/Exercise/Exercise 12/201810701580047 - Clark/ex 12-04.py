# Exercise 12-04
'''
name:Clark
class:net182
I  D:201810701580047
'''
from abc import ABC, abstractmethod
import math


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


class Circle(Shape, ABC):
    def __init__(self, colour, radius):
        Shape.__init__(self, colour)
        self.radius = radius

    def get_area(self):
        return self.radius * math.pi

    def draw(self):
        print('Drawing a circle')


shapes = [Circle("Blue", 10), Circle("White", 20), Rectangle("Black", 3, 5), Rectangle("Red", 7, 9)]
for a in shapes:
    a.fill()
    a.draw()
total_area = 0
max_area = shapes[0].get_area()
min_area = shapes[0].get_area()
for b in shapes:
    total_area += b.get_area()
    if max_area < b.get_area():
        max_area = b.get_area()
    if min_area > b.get_area():
        min_area = b.get_area()
average_area = total_area/len(shapes)
print('%.2f' % total_area)
print('%.2f' % average_area)
print('%.2f' % float(max_area))
print('%.2f' % float(min_area))
