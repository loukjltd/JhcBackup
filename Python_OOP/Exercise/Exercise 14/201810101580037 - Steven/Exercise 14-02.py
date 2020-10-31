# exercise14-02
'''
student name: Steven
ID: 201810101580037
class: network 182
'''
f=open('my_text2.txt','r')
a=[]
for i in f.readlines():
    a.append(int(i))
print('Sum : '+str(sum(a)))
