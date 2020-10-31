'''
Class:Net182
Name:Assass
ID:201810701580040
'''
def calculate_area_rectangle(width,height):
    return width*height
def calculate_perimeter_rectangle(width,height):
    return 2*(width+height)
def calculate_area_circle(radius):
    return 3.142*radius*radius
def calculate_circumference(radius):
    return 2*3.142*radius
w=float(input('Enter the width of the rectangle:'))
h=float(input('Enter the length of the rectangle:'))
r=float(input('Enter the radius of the circle: '))
print('The area of the rectangle is:'+str(calculate_area_rectangle(w,h)))
print('The perimeter of the rectangle is:'+str(calculate_perimeter_rectangle(w,h)))
print('The area of the circle is:'+str(format(calculate_area_circle(r),'.3f')))
print('The circumference of the circle is:'+str(format(calculate_circumference(r),'.2f')))