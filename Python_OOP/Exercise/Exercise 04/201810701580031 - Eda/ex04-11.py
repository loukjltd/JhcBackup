# exercise 04-11
'''
student name: Eda
ID: 201810701580031
class: network182
'''


print('M   T   W   T   F   S   Su',end = '\t')
print( )
for i in range(1,32):
    print(i,end = '\t')
    if i % 7 == 0:
        print( )