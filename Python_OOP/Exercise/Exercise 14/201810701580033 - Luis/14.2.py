
# exercise 14-02
'''
student name: Luis
ID: 201810701580033
class: network182
'''

f=open("./my_text2.txt",'r')
s=0
for i in f.readlines():
    s=s+int(i)
print("Sum="+str(s))