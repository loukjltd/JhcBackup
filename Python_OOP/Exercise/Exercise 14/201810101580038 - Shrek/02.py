#exercise 14-02
'''
class: net182
studentid:201810101580038
studentname:shrek
'''
f=open('C:\yourname\my_text2.txt','r')
a=[]
for i in f.readlines():
    a.append(int(i))
print('Sum : '+str(sum(a)))