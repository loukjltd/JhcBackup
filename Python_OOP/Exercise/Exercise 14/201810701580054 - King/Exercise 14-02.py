# Exercise 014-02
'''
name: King
idnumber: 201810701580054
class: net182
'''
f=open('F:\python\my_text2.txt','r')
a=[]
for i in f.readlines():
    a.append(int(i))
print('Sum : '+str(sum(a)))