#Exercise 04-08
'''
#name: King
idnumber: 201810701580054
class: net182
'''

unser=input("enter english:")
a=0
for i in unser:
    if i in ('a','e','i','o','u'):
        print('X',end=' ')
        a+=1
    else:
        print(i,end=' ')
print()
print('\d','There are '+str(a)+' vowels in the word or sentence.')