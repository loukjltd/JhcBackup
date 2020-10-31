'''
student name: Eden
#ID: 201810701580060
#class: net182
'''
price={'Banana':4,'Apple':2,'Orange':1.5,'Pear':3}
quantity ={'Banana':1,'Apple':0,'Orange':3,'Pear':2}
sum = 0
for i in price :
    for j in quantity:
        if i==j:
            sum = sum + price[i]*quantity[j]
print('Total cost: ',sum)