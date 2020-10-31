# Exercise 014-02
'''
Student Name: Leo
ID: 201810701580053
Class: Network 182
'''
f=open('F:\python\my_text2.txt','r')
a=[]
for i in f.readlines():
    a.append(int(i))
print('Sum : '+str(sum(a)))
