'''
Class:Net182
Name:Assass
ID:201810701580040
'''
class Shape:
    def __init__(self,colour):
        self.colour=colour
    def colour(self):
        return self.colour
class Rectangle(Shape):
    def __init__(self,colour,width,height):
        Shape.__init__(self,colour)
        self.__width=int(width)
        self.__height=int(height)
    def calculate_area(self):
        return str(float(self.__width*self.__height))
class Triangle(Shape):
    def __init__(self,colour,width,height):
        Shape.__init__(self,colour)
        self.__width=int(width)
        self.__height=int(height)
    def calculate_area(self):
        return str(float(self.__width*self.__height/2))

rec1 = Rectangle("red", 4, 5)
print(rec1.colour)
print(rec1.calculate_area())

tri1 = Triangle("blue", 6, 8)
print(tri1.colour)
print(tri1.calculate_area())
