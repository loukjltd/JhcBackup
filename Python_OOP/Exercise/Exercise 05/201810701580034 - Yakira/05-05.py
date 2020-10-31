# exercise 05-05
'''
student name : Yakira
ID : 201810701580034
class : Net182
'''
price = {'Banana':4,'Apple':2,'Orange':1.5,'Pear':3}
quantity = {'Banana':1,'Apple':0,'Orange':3,'Pear':2}
sum = 0
total = 0
for key in price :
    sum = price[key]*quantity[key]
    int(sum)
    total += sum
print('Total cost: ',total)


