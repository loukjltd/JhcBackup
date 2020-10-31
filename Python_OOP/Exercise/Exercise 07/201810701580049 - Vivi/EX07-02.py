#Exercise 07-02
'''
class net182
id 2018100701580049
name vivi
'''
width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))
radius = float(input("Enter the radius of the circle: "))
def calculate_area_rectangle(width,height):
    info = "The area of the rectangle is: "
    result = str(width * height)
    return info + result

def calculate_perimeter_rectangle(width,height):
    info = "The perimeter of the rectangle is: "
    result = str((width + height) * 2)
    return info + result

def calculate_area_circle(radius):
    info = "The area of the circle is: "
    circle = 3.141
    result = str(float((radius ** 2 ) * circle))
    return info + result

def calculate_circumference(radius):
    info = "The circumference of the circle is: "
    circle = 3.141
    result = '%.2f' % float(2 * radius * circle)
    return info + result

print()

print(calculate_area_rectangle(width,height))
print(calculate_perimeter_rectangle(width,height))
print(calculate_area_circle(radius))
print(calculate_circumference(radius))
