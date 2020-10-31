

# Exercise 07-02
''''
student name:Luis
ID:201810701580033
class:network 182
'''


width=float(input("Enter the width of the rectangle:"))
height=float(input("Enter the height of the rectangle:"))
r=float(input("Enter the radius of the circle: 5"))
def calculate_area_rectangle():
    area=width*height
    return area
def calculate_perimeter_rectangle():
    perimeter=(width+height)*2
    return perimeter
def calculate_area_circle():
    circlearea=3.14*r**2
    return circlearea
def calculate_circumference():
    circumference=2*r*3.14
    return circumference

print("The area of the rectangle is:"+str(calculate_area_rectangle()))
print("The perimeter of the rectangle is:"+str(calculate_perimeter_rectangle()))
print("The area of the circle is:"+str(calculate_area_circle()))
print("The circumference of the circle is:"+str(calculate_circumference()))


