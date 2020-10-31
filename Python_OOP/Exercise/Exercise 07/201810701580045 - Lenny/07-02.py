def calculate_area_rectangle(width,height):
    area = width * height
    return area

def calculate_perimeter_rectangle(width,height):
    perimeter = (width + height) * 2
    return perimeter

def calculate_area_circle(radius):
    area = radius * radius * 3.14
    return area

def calculate_circumference(radius):
    circumfernce = 2 * 3.14 * radius
    return circumfernce

number1 = int(input('Enter the width of the rectangle: '))
number2 = int(input('Enter the length of the rectangle: '))
number3 = int(input('Enter the radius of the circle: '))

print('The area of the rectangle is: ' + str(calculate_area_rectangle(number1,number2)))
print('The perimeter of the rectangle is: ' + str(calculate_perimeter_rectangle(number1,number2)))
print('The area of the circle is: ' + str('%.3f' % calculate_area_circle(number3)))
print('The circumference of the circle is: ' + str('%.2f' % calculate_circumference(number3)))