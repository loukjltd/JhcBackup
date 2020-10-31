# exercise 04-11
'''
student name : Yakira
ID : 201810701580034
class : Net182
'''
print('M   T   W   T   F   S   Su \n')
s = 0

while s < 32:
    for i in  range(5):
        print (str(s+1)+'   '+str(s+2)+'   '+str(s+3)+'   '+str(s+4)+'   '+str(s+5)+'   '+str(s+6)+'   '+str(s+7))
        s = s + 7
    print(end="\t")