#net171 ZERO
def calculateAreaRectangle(width,height):
    area=width*height
    return area
def calculatePerimeterRectangle(width,height):
    perimeter=(width+height)*2
    return perimeter
def calculateAreaCircle(radius):
    area=radius*radius*3.14
    return area
def calculateCircumference(radius):
    circumference=radius*2*3.14
    return circumference

print(calculateAreaRectangle(4,5))
print(calculatePerimeterRectangle(4,5))
print(calculateAreaCircle(4))
print(calculateCircumference(4))