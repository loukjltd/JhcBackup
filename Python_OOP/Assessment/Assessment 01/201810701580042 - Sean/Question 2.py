# Assessment 1 Question 2
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''

radius = float(input('Enter the radius: '))
pi = 3.1416
template1 = "{0:10} {1:10} {2:10}"
template2 = "{0:15} {1:10} {2:10}"
line1 = template1.format('Radius', 'Area', 'Perimeter')
print(str(line1))
print('_______________________________')
area = radius * radius * pi
perimeter = radius * 2 * pi
line3 = template1.format(str(radius), str('%.2f' % area), str('%.2f' % perimeter))
print(str(line3))
