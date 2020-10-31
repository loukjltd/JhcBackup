'''
student name: Eden
#ID: 201810701580060
#class: net182
'''
width =int(input("Enter the width of the rectangle:  "))
height = int(input("Enter the length of the rectangle:  "))
radius = int(input("Enter the radius of the circle:  "))

def calculate_area_rectangle(width,height):
    return width * height
def calculate_perimeter_rectangle(width,height):
    return width * 2 + height * 2
def calculate_area_circle(radius):
    return radius * radius * 3.14
def calculate_circumference(radius):
    return radius * 2 * 3.14

print("The area of the rectangle is: " + str(calculate_area_rectangle(width, height)))
print("The perimeter of the rectangle is: " + str(calculate_perimeter_rectangle(width,height)))
print("The area of the circle is: " + str(float(calculate_area_circle(radius))))
print("The circumference of the circle is:  " + str(float(calculate_circumference(radius))))