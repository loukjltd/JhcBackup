'''
student name:Bruce
ID:201810701580057
class: network 182
'''


class Shape:
    def __init__(self,color):
        self.__color = color
    def color(self):
        return self.__color
class Rectangle(Shape):
    def __int__(self,color,width,height):
        Shape.__init__(self,color)
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Triangle(Shape):
    def __int__(self,color,width,height):
        Shape.__init__(self,color)
        self.width = width
        self.height = height
    def area(self):
        return (self.width * self.height)/2

rec1 = Rectangle('red',4,5)

print(rec1.area())

tri1 = Triangle('blue',6,8)

print(tri1.area())