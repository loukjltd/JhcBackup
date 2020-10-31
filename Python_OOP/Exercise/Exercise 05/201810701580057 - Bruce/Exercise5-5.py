#Exercise5-5
'''
student name:Bruce
ID:201810701580057
class: network 182
'''
price = {'Banana' : 4,'Apple' : 2,'Orange' : 1.5,'pear' : 3}
quantity = {'Banana' : 1,'Apple' : 0,'Orange' : 3,'pear' : 2}

sum = 0

for i in price:
    sum += (price[i] * quantity[i])
print('Total cost: ',sum)