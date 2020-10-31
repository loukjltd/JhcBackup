#Exercise 04-11
'''
name: Assass
idnumber: 201810701580040
class: network 182
'''
print('M\t','T\t','W\t','T\t','F\t','S\t','Su\r',)
for i in range(1,32):
    print(i,end='\t')
    if i%7==0:
        print()