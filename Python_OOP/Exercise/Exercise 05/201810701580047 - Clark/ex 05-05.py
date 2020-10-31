# Exercise 05-05
'''
name:Clark
class:net182
I  D:201810701580047
'''
price = {'Banana': 4, 'Apple': 2, 'Orange': 1.5, 'Pear': 3}
quantity = {'Banana': 1, 'Apple': 0, 'Orange': 3, 'Pear': 2}
sum = 0
for a in price:
    sum += price[a] * quantity[a]
print('Total cost:', sum)
