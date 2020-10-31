#exercise 02
'''
studentname:Tami
student id:201810701580035
class:net182
'''

radius = float(input('Enter the radius: '))
TT = 3.1416
template1 = "{0:10} {1:10} {2:10}"
template2 = "{0:15} {1:10} {2:10}"
result1 = template1.format('Radius', 'Area', 'Perimeter')
print(str(result1))
print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _')
area = radius * radius * TT
perimeter = radius * 2 * TT
result2 = template1.format(str(radius), str('%.2f' % area), str('%.2f' % perimeter))
print(str(result2))
