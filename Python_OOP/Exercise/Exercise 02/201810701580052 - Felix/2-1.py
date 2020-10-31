# Exercise 02-01
'''
student name: felix
#ID: 201810701580052
#class: net182
'''
meal = 44.50
tax = 0.0675
tip = 0.15
meal = meal + meal*tax
total = meal+meal*tip
t1 = '{0:<4.2f}'
r1 = t1.format(total)
print('Total cost of meal: $',r1)