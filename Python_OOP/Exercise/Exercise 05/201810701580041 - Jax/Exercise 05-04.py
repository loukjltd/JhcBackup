#Exercise 05-04
'''
name: Jax
idnumber: 201810701580041
class: net182
'''

marks={}
marks['Sam']=90.5
marks['Jane']=85.4
marks['Max']=92.3
marks['Alice']=64.5
marks['John']=69.4
sum=0
for i in marks.values():
    sum+=i
print('sum = '+str(sum))
print('Average: '+str(sum/len(marks.values())))