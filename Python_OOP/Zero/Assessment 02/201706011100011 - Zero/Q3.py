class Shape:
    def __init__(self, colour):
        self.colour = colour

    def get_shape_type(self):
        return "General shape"


class Rectangle(Shape):
    def __init__(self, colour, width, height):
        Shape.__init__(self, colour)
        self.width = width
        self.height = height

    def get_shape_type(self):
        return "Rectangle"

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height


rectangle_list1 = [Rectangle("white", 4, 3),
                    Rectangle("red", 9, 5),
                    Rectangle("purple", 3, 6),
                    Rectangle("orange", 15, 10),
                    Rectangle("black", 4, 14)]

rectangle_list2 = [Rectangle("pink", 3, 4),
                    Rectangle("red", 10, 2),
                    Rectangle("white", 8, 5),
                    Rectangle("blue", 14, 4),
                    Rectangle("grey", 10, 15)]

colours = 0
perimeters = 0
for i in rectangle_list1:
    for j in rectangle_list2:
        if i.colour == j.colour:
            colours = colours+1
        if i.get_perimeter() == j.get_perimeter():
            perimeters = perimeters + 1


print("There are %s rectangle objects with the same colours" % (colours))
print("There are %s rectangle objects with the same colours" % (perimeters))
