'''
student name:Bruce
ID:201810701580057
class: network 182
'''


import math

a = int(input('Enter the width of the rectangle: '))
b = int(input('Enter the length of the rectangle: '))
c = int(input('Enter the radius of the circle: '))
def calculate_area_rectangle(a,b):
    rectangle_area = a * b
    return rectangle_area
print('The area of the rectangle is: ' + str(calculate_area_rectangle(a,b)))

def calculate_perimeter_rectangle(a,b):
    rectangle_perimeter = (a + b) * 2
    return rectangle_perimeter
print('The perimeter of the rectangle is: ' + str(calculate_perimeter_rectangle(a,b)))

def calculate_area_circle(c):
    circle_area = c * c * math.pi
    return circle_area
print('The area of the circle is: ' + str('%.3f' % calculate_area_circle(c)))
def calculate_circumference(c):
    circle_circumference = 2 * math.pi * c
    return circle_circumference
print('The circumference of the circle is: '+ str('%.2f' % calculate_circumference(c)))
