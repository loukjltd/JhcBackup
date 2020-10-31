#Exercise 04-11
'''
Name:Lester
ID:201810701580055
Class:Net 182
'''

print('M\t','T\t','W\t','T\t','F\t','S\t','Su\r',)
for i in range(1,32):
    print(i,end='\t')
    if i%7==0:
        print()
