'''
exercise: 07-02
class:net182
name:Lee
ID:201810101580036
'''
def calculate_area_rectangle(width,height):
    area = width * height
    return area
def calculate_perimeter_rectangle(width,height):
    perimeter = (width + height)*2
    return perimeter
def calculate_area_circle(radius):
    area = radius * 3.14 * 2
    return area
def calculate_circumference(radius):
    circumference = radius * 2 * 3.14
    return circumference
width = int(input('Enter the width of the rectangle: '))
length = int(input('Enter the length of the rectangle: '))
radius = int(input('Enter the radius of the circle: '))
print('The area of the rectangle is: ' + str(calculate_area_rectangle(width,length)))
print('The perimeter of the rectangle is: ' + str(calculate_perimeter_rectangle(width,length)))
print('The area of the circle is: ' + str('%.2f'%calculate_area_circle(radius)))
print('The circumference of the circle is: ' + str('%.2f'%calculate_circumference(radius)))