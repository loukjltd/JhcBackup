#Exercise 05-05
'''
name:leo
idnumber: 201810701580053
class: net182
'''

price={'Banana':4,'Apple':2,'Orange':1.5,'Pear':3}
quantity={'Banana':1,'Apple':0,'Orange':3,'Pear':2}
sum=0
for i in price:   #遍历键名
    sum+=price[i] * quantity[i]  #同键名，所以直接用i这个keys就可以了
print('Total cost: '+str(sum))
