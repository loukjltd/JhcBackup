'''
class:net182
name:Lee
ID:201810101580036
'''
f = open('D:\yourname\my_text2.txt','r')
s = 0

for x in f.readlines():
    s += int(x)
print(s)
