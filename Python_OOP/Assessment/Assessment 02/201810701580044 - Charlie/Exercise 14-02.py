# Exercise 014-02
'''
Student Name: Charlie
ID: 201810701580044
Class: Network 182
'''
f=open('F:\python\my_text2.txt','r')
a=[]
for i in f.readlines():
    a.append(int(i))
print('Sum : '+str(sum(a)))