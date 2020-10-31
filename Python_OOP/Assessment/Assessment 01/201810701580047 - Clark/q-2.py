# Question 2
'''
name:Clark
class:net182
I  D:201810701580047
'''
r = float(input('Enter a radius: '))
area = float(r) * float(r) * 3.1416
perimeter = float(r) * 6.2832
print('{0:<10}{1:<10}{2:>11}'.format('Radius', 'Area', 'Perimeter'))
print('-------------------------------')
print('{0:<10.2f}{1:<10.2f}{2:>10.2f}'.format(r, area, perimeter))
