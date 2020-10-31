# exercise 02-01
'''
student name: Yakira
ID: 201810701580034
class: network 182
'''
meal = 44.50
tax = 0.0675
tip = 0.15
meal = meal+meal*tax
total = meal+meal*tip
tax1 = tax*100
tip1 = tip*100

print('Total cost of meal: ${0:.2f}'.format(total))
print('Restaurant tax: {0:.2f} %'.format(tax1))
print('Tip: {0:<.0f} %'.format(tip1))
