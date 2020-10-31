#Exercise 04-11
'''
name: King
idnumber: 201810701580054
class: net182
'''

print('M\t','T\t','W\t','T\t','F\t','S\t','Su\r',)
for i in range(1,32):
    print(i,end='\t')
    if i%7==0:
        print()