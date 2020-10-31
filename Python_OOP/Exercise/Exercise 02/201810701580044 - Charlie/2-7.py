'''
student name: Charlie
ID: 201810701580044
class: network 182
'''

a = input('Enter an animal:')
print(a)

b = input('Enter the first number:')
c = input('Enter the second number:')
d = int(b) + int(c)
print('Answer','=',d)

e = input('Enter the length of the rectangle:')
f = input('Enter the width of the rectangle:')
Area = float(e) * float(f)
Perimeter = (float(e)+float(f)) * 2
print('Area','=',Area)
print('Perimeter','=',Perimeter)

g = input('Enter the radius of the circle:')
Area = 3.14 * float(g)**2
print('Area','=',Area)