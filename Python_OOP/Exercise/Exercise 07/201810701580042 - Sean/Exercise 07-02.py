# Exercise 07-02
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''


def calculate_area_rectangle(width, height):
    area = width * height
    return area


def calculate_perimeter_rectangle(width, height):
    perimeter = (width + height) * 2
    return perimeter


def calculate_area_circle(radius):
    area = 3.14159 * radius * radius
    return area


def calculate_circumference(radius):
    circumference = 3.14159 * radius * 2
    return circumference


w = int(input('Enter the width of the rectangle: '))
l = int(input('Enter the length of the rectangle: '))
r = int(input('Enter the radius of the circle: '))

print('The area of the rectangle is: ' + str(calculate_area_rectangle(w, l)))
print('The perimeter of the rectangle is: ' + str(calculate_perimeter_rectangle(w, l)))
print('The area of the circle is: ' + str('%.3f' % calculate_area_circle(r)))
print('The circumference of the circle is: ' + str('%.2f' % calculate_circumference(r)))

