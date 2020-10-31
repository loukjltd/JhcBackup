#Exercise 07-02
#Josh net182 201810701580043

def calculate_area_rectangle(width, height):
    return width*height

def calculate_perimeter_rectangle(width, height):
    return 2*(width + height)

def calculate_area_circle(radius):
    return radius**2*3.141

def calculate_circumference(radius):
    return radius*2*3.141

wid = int(input('Enter the width of the rectangle: '))
hei = int(input('Enter the length of the rectangle: '))
rad = float(input('Enter the radius of the circle: '))
print()
print('The area of the rectangle is: '+str(calculate_area_rectangle(wid,hei)))
print('The perimeter of the rectangle is: '+str(calculate_perimeter_rectangle(wid, hei)))
print('The area of the circle is: '+str(calculate_area_circle(rad)))
print('The circumference of the circle is:'+str(calculate_circumference(rad)))