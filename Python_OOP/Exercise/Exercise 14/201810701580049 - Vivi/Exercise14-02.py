#Exercise 14-02
"""
class:net182
name:vivi
id:201810701580049
"""
f = open("my_text2.txt",'r')
num = 0
for i in f.readlines():
    num += int(i)
print("Sum: {}".format(num))
