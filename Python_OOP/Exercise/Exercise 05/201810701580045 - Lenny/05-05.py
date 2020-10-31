#exercise 05-05
'''
name:Lenny
class:net182
ID:201810701580045
'''
price = {'Banana':4,'Apple':2,'Orange':1.5,'Pear':3}
quantity = {'Banana':1,'Apple':0,'Orange':3,'Pear':2}
sum = 0
for i in price.keys():
    sum += price[i] * quantity[i]
print('Total cost:' + str(sum))