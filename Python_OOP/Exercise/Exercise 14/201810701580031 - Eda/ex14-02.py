# exercise 14-02
'''
student name: Eda
ID: 201810701580031
class: network182
'''
f = open("./my_text2.txt","r")
num = []
for i in f.readlines():
    num.append(int(i))
print("sum: " ,sum(num))