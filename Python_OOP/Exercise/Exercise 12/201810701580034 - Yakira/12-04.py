# exercise 12-04
'''
student name: Yakira
ID: 201810701580034
class: network182
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
    def draw(self):
        pass
class Rectangle(Shape):

    def __init__(self, colour, length, width):
        Shape.__init__(self,colour)
        self.colour = colour
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def draw(self):
        print("Drawing a rectangle")
class Circle(Shape):
    def __init__(self,colour,radius):
        Shape.__init__(self,colour)
        self.colour = colour
        self.radius = radius
    def get_area(self):
        return math.pi*self.radius**2
    def draw(self):
        print("Drawing a circle")
shapes = [Circle("Blue", 10),
           Circle("White", 20),
           Rectangle("Black", 3, 5),
           Rectangle("Red", 7, 9)]
for Shape in shapes:
    Shape.fill()
    Shape.draw()

total_area = 0
max_area = shapes[0].get_area()
min_area = shapes[0].get_area()

for i in shapes:
    areal = i.get_area()
    total_area = total_area + areal
    if areal > max_area:
        max_area = areal
    if areal < min_area:
        min_area = areal
average_area=(total_area/len(shapes))

print(str('%.2f'%(total_area)))
print(str('%.2f'%(average_area)))
print(str('%.2f'%(max_area)))
print(str('%.2f'%(min_area)))