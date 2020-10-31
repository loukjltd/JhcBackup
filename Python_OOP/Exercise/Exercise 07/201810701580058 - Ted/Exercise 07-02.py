# Exercise 07-02
'''
Student Name: Ted
ID: 201810701580058
Class: Net 182
'''

def calculate_area_rectangle(width,height):
    area=width*height
    return area
def calculate_perimeter_rectangle(width,height):
    perimeter = (width+height)*2
    return perimeter
def calculate_area_circle(radius):
    area_circle=pow(radius,2)*3.141
    return area_circle
def calculate_circumference(radius):
    circumference=2*radius*3.141
    return circumference
width = int(input('enter a number:'))
height = int(input('enter a number:'))
radius=float(input('enter a number:'))
print()
print('The area of the rectangle is: '+str(calculate_area_rectangle(width,height)))
print('The perimeter of the rectangle is: '+str(calculate_perimeter_rectangle(width,height)))
print('The area of the circle is: '+str(calculate_area_circle(radius)))
print('The circumference of the circle is: '+str(calculate_circumference(radius)))
