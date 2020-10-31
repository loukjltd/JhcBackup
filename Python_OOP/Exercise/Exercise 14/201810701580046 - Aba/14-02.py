'''
class:net182
name:Aba
ID:201810701580046
'''
f = open('D:\yourname\my_text2.txt','r')
s = 0

for x in f.readlines():
    s += int(x)
print(s)
