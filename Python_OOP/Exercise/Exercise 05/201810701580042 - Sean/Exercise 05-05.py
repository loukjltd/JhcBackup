# Exercise 05-05
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''

price = {}
price['Banana'] = 4
price['Apple'] = 2
price['Orange'] = 1.5
price['Pear'] = 3
quantity = {}
quantity['Banana'] = 1
quantity['Apple'] = 0
quantity['Orange'] = 3
quantity['Pear'] = 2
sum = 0

for p in price:
    sum += price[p] * quantity[p]
print('Total cost: ' + str(sum))
