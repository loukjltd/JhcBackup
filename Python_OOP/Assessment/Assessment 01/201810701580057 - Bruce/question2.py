'''
student name:Bruce
ID:201810701580057
class: network 182
'''

Radius = float(input('Enter a radius: '))
TT = 3.1416

Area = Radius * Radius * TT

Perimeter = Radius * 2 * TT

template = '{0:<10}{1:>5}{2:>20}'
result1 = template.format('Radius','Area','Perimeter')
print(result1)
print('-----------------------------------')
result2 = template.format(str(Radius),str('%.2f' % Area),str('%.2f' % Perimeter))
print(result2)