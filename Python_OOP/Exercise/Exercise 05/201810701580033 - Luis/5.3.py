# Exercise 05-03
''''
student name:Luis
ID:201810701580033
class:network 182
'''

d={}
d = {'Name': 'James', 'Age': 21, 'Course': 'IT','ID':'2016A001'}
d['Name'] = 'James'
d['Age'] = 21
d['Course'] = 'IT'
d['ID']= '2016A001'
print(d)
print(d['Name'],d['ID'])

del d['Course']
print(d)
for key in d:
    print(d[key])



