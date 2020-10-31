# exercise 14 02
'''
Bro
201810701580056
network 182
'''
f=open('.\my_text2.txt','r')
a=[]
for i in f.readlines():
    a.append(int(i))
print('Sum : '+str(sum(a)))