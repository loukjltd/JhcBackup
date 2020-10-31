# exercise 07 02
'''
Bro
201810701580056
network 182
'''
a = int(input('Enter the width of the rectangle: '))
b = int(input('Enter the length of the rectangle: '))
c = int(input('Enter the radius of the circle: '))
def calculate_area_rectangle():
    area_rectangle=a*b
    return area_rectangle
def calculate_perimeter_rectangle():
    perimeter_rectangle=(a+b)*2
    return perimeter_rectangle
def  calculate_area_circle():
    area_circle=c*c*3.14
    return area_circle
def  calculate_circumference():
    circumference_circle=2*3.14*c
    return circumference_circle

print('The area of the rectangle is: ',calculate_area_rectangle())
print('The perimeter of the rectangle is: ',calculate_perimeter_rectangle())
print('The area of the circle is: ',calculate_area_circle())
print('The circumference of the circle is: ',calculate_circumference())