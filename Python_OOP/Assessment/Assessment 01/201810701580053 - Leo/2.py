'''
Student Name: leo
ID: 201810701580053
Class: Network 182
'''
R = int(input('enter a radius :'))
b = R*R*3.14
c = 2*3.14 *R
template = "{0:<15}{1:<15}{2:>10}"
result = template.format("Radius", "Area","Perimeter")
print(result)
print('-------------------------------------')
template1= "{0:<15.2f}{1:<15.2f}{2:>10.2f}"
result1 = template.format(R, b,c)
print(result1)
