# Exercise 14-02
'''
student name: felix
#ID: 201810701580052
#class: net182
'''
r = open('.\my_text2.txt','r')
s = 0
for i in r.readlines():
    s = s + int(i)
print('Sum: ',s)
