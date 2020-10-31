# Exercise 01-04
'''
student name: felix
#ID: 201810701580052
#class: net182
'''
t1 = '{0:<10}{1:>5}'
r1 = t1.format('Name','Score')
Max = 77.234
Alice = 89.325235
Bob = 68
t2 = '{0:<10}{1:>5.1f}'
r2 = t2.format('Max',Max)
r3 = t2.format('Alice',Alice)
r4 = t2.format('Bob',Bob)
print(r1)
print(r2)
print(r3)
print(r4)