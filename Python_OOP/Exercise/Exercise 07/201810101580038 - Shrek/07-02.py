#exercise 07-02
'''
student name:shrek
student id:201810101580038
class:net182
'''
import math
width = int(input('Enter the width of the rectangle: '))
height = int(input('Enter the length of the rectangle: '))
radius= int(input('Enter the radius of the circle: '))

def calculate_area_rectangle(width,height):
    area =width*height
    return area
print('The area of the rectangle is: '+str(calculate_area_rectangle(width,height)))

def calculate_perimeter_rectangle(width,height):
    perimetre=(width+height)*2
    return perimetre
print('The perimeter of the rectangle is: '+ str(calculate_perimeter_rectangle(width,height)))
def calculate_area_circle(radius):
    area = radius *radius* math.pi
    return area
print('The area of the circle is: '+str('%.3f' % calculate_area_circle(radius)))
def calculate_circumference(radius):
    circumference=math.pi * 2 *radius
    return circumference

print('The circumference of the circle is '+str('%.2f'% calculate_circumference(radius)))

