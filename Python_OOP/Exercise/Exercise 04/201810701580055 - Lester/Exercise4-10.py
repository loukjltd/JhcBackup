#Exercise 04-10
'''
Name:Lester
ID:201810701580055
Class:Net 182
'''

a=int(input('Enter the number for the times table:'))
for i in range(1,a+1):
    for o in range(1,a+1):
        print(i*o,end='\t')
    print()
