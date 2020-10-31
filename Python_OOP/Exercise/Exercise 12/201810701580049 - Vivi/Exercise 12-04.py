#Exercise 12-04
"""
Class:Net182
name:vivi
id:201810701580049
"""
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
    def __init__(self,color,radius):
        Shape.__init__(self,color)
        self.radius = radius

    def get_area(self):
        return self.radius * self.radius * 3.141

    def draw(self):
        print("Drawing a Circle")
shapes = [Circle("Blue", 10),
          Circle("White", 20),
          Rectangle("Black", 3, 5),
          Rectangle("Red", 7, 9)]

for i in shapes:
    i.fill()
    i.draw()

total_area = 0
max_area = shapes[0].get_area()
min_area = shapes[0].get_area()

for o in shapes:
    area1 = o.get_area()
    total_area += area1

    if area1 > max_area:
        max_area = area1
    if area1 < min_area:
        min_area = area1


print("Total: {0:.2f}".format(total_area))
print("Average: {0:.2f}".format(total_area/len(shapes)))
print("Max: {0:.2f}".format(max_area))
print("Min: {0:.2f}".format(min_area))
