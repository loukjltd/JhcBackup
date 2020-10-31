#exercise 05-05
'''
student name: shrek
student id:201810101580038
class:net 182
'''



price = {'banana':4,'apple':2,'orange':1.5,'pear':3}
quantity = {'banana':1,'apple':0,'orange':3,'pear':2}
sum=0
for key in price:
    sum+=price[key]*quantity[key]
print('Total cost :',sum)
