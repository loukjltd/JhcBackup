'''
student name: leo
ID: 201810701580053
class: network182
'''
yn='y'
i=[]
a=0
while yn !='n' and yn!='N':
    num=int(input('Enter a number:'))
    i.append(num)
    a+=1
    yn=input('Do you want to enter another number?:')
print('Sum = '+str(sum(i)))
print('Average = '+str(sum(i)/a))
