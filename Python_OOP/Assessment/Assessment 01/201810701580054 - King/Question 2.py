#Question 2
'''
name: King
idnumber: 201810701580054
class: net182
'''

radius = float(input('Enter the radius: '))
TT = 3.1416
template1 = "{0:10} {1:10} {2:10}"
template2 = "{0:15} {1:10} {2:10}"
line1 = template1.format('Radius', 'Area', 'Perimeter')
print(str(line1))
print('-----------------------------------------------------')
area = radius * radius * TT
perimeter = radius * 2 * TT
line3 = template1.format(str(radius), str('%.2f' % area), str('%.2f' % perimeter))
print(str(line3))