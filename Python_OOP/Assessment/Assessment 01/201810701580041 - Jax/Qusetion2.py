# Qusetion2
'''
Student Name: Jax
ID: 201810701580041
Class: Net 182
'''

def calculate_area_circle(radius):
    area_circle=pow(radius,2)*3.1416
    return area_circle
radius=float(input('enter a radius: '))
def calculate_circumference(radius):
    circumference=2*radius*3.1416
    return circumference
print('Enter a radius: '+str(radius))
a=str(calculate_area_circle(radius))
b=str(calculate_circumference(radius))
template = "{0:<10}{1:>15}{2:>20}"
result = template.format("Radius", "Area",'Perimeter')
print(result)
print('-----------------------------------')
c=template.format('8',a,b)
print(c)
