'''
name:Lee
class:net182
id:201810101580036
'''
from abc import ABC,abstractclassmethod
class Shape(ABC):
    def __init__(self,colour):
        self.colour = colour
    def fill(self):
        print('Shape filled with {0}'.format(self.colour))
    @abstractclassmethod
    def get_area(self):
        pass
    def draw(self):
        pass
class Rectangle(Shape):
    def __init__(self,colour,length,width):
        Shape.__init__(self,colour)
        self.length = length
        self.width = width
    def get_area(self):
        return self.length * self.width
    def draw(self):
        print('Drawing a rectangle')
class Circle(Shape):
    def __init__(self,colour,radius):
        Shape.__init__(self,radius)
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius * self.radius
    def draw(self):
        print('Drawing a circle')
shapes_list = [Circle('Blue',10),
               Circle('White',20),
               Rectangle('Black',3,5),
               Rectangle('Red',7,9)]
for s in shapes_list:
    s.fill()
    s.draw()
total_area = 0
max_area = 0
min_area = shapes_list[0].get_area()
for s in shapes_list:
    areal = s.get_area()
    total_area = total_area + areal
    if areal > max_area:
        max_area = areal
    if areal < min_area:
        max_area = areal
print('Total : {0:.2f}'.format(total_area))
print('Average : {0:.2f}'.format(total_area/len(shapes_list)))
print('Maximum area : {0:.2f}'.format(max_area))
print('Minimum area : {0:.2f}'.format(min_area))
