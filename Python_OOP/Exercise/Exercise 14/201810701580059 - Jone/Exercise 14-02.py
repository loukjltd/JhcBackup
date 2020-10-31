# Exercise 014-02
'''
Student Name: jone
ID: 201810701580059
Class: Network 182
'''
f=open('my_text2.txt','r')
a=[]
for i in f.readlines():
    a.append(int(i))
print('Sum : '+str(sum(a)))