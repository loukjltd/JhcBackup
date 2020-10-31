# Question 2
'''
student name: Steven
ID: 201810101580037
class: network 182
'''
radius = float(input('Enter a radius: '))
pai = 3.1415
template1 = "{0:10} {1:10} {2:10}"
line1 = template1.format('Radius', 'Area', 'Perimeter')
print(line1)
print('_______________________________')
print()
area = radius * radius * pai
perimeter = radius * 2 * pai
line2 = template1.format(str(radius), str('%.2f' % area), str('%.2f' % perimeter))
print(line2)
