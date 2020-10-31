# Exercise 09-03
'''
Student Name: Ted
ID: 201810701580058
Class: Network 182
'''
class Shape:
    def __init__(self,colour):
        self.colour=colour
class Rectangle(Shape):
    def __init__(self,colour,width,height):
        Shape.__init__(self,colour)
        self.width=width
        self.height=height
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    def calculate_area(self):
        return float(self.width*self.height)
class Triangle(Shape):
    def __init__(self,colour,width,height):
        Shape.__init__(self,colour)
        self.width=width
        self.height=height
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    def calculate_area(self):
        return float(self.width*self.height)/2
rec1 = Rectangle("red", 4, 5)
print(rec1.colour)
print(rec1.calculate_area())

tri1 = Triangle("blue", 6, 8)
print(tri1.colour)
print(tri1.calculate_area())
