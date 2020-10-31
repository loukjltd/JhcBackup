# exercise05-05
'''
student name: Steven
ID: 201810101580037
class: network 182
'''
Price = {'Banana':4,'Apple':2,'Orange':1.5,'Pear':3}
Quantity = {'Banana':1,'Apple':0,'Orange':3,'Pear':2}
sum = 0
for i in Price :
    sum = Price[i] * Quantity[i] + sum
print("Total cost:" + str(sum))

