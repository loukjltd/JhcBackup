# exercise 07-02
'''
student name: Eda
ID: 201810701580031
class: network182
'''

a = int(input("Enter the width of the rectangle:"))
b = int(input("Enter the length of the rectangle:"))
c = int(input("Enter the radius of the circle:"))
def calculate_area_rectangle():
    area = a * b
    return area

def calculate_perimeter_rectangle():
    permeter = (a + b) * 2
    return permeter


def calculate_area_circle():
    area1 = 3.14 * c ** 2
    return area1


def calculate_circumference():
    circumference = 2 * 3.14 * c
    return circumference
print('The area of the rectangle is: ' + str(calculate_area_rectangle( )))
print('The perimeter of the rectangle is:' + str(calculate_perimeter_rectangle()))
print('The area of the circle is:' + str('%.2f'% calculate_area_circle()))
print('The circumference of the circle is:' + str('%.3f'% calculate_circumference()))