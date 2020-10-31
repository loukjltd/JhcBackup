#Exercise 04-013
'''
name: Jax
idnumber: 201810701580041
class: net182
'''

number=int(input('Enter a number: '))
a=[]
ask=input('Do you want to enter another number?(y or n):')
b=1
a.append(number)
while ask!='n':
    number = int(input('Enter a number: '))
    a.append(number)
    b+=1
    ask=input('Do you want to enter another number?(y or n):')

else:
    print('Sum = '+str(sum(a)))
    print('Average = '+str(sum(a)/b))
