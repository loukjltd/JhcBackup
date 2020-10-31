'''
class:net182
name:Assass
id:201810710580040
'''
import re as re
f = open("./my_text2.txt", "r")
sum1=[]

for i in f.readlines():
    i =int(re.sub('[\n]', '', i))
    sum1.append(i)

print('Sum:',str(sum(sum1)))