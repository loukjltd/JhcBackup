h = input('Enter the length of the rectangle: ')
w = input('Enter the width of the rectangle: ')
r = input('Enter the radius of the circle: ')


def calculate_area_rectangle(height, width):
    area = int(height) * int(width)
    return area


def calculate_perimeter_rectangle(height, width):
    perimeter = (height + width) * 2
    return perimeter


def calculate_area_circle(radius):
    area = int(radius) * int(radius) * 3.14
    return area


def calculate_circumference(radius):
    circumference = int(radius) * 6.28
    return circumference


print('The area of the rectangle is:', calculate_area_rectangle(h, w))
print('The perimeter of the rectangle is:', calculate_perimeter_rectangle(h, w))
print('The area of the circle is:', calculate_area_circle(r))
print('The circumference of the circle is:', '{0:.2f}'.format(calculate_circumference(r)))
