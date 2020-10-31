# exercise 04-13
'''
student name: Eda
ID: 201810701580031
class: network182
'''


count=0
a = 0
b = True
while b == True:
    c = int(input('Enter a number:'))
    d = input('Do you want enter another number?')
    count += 1
    a = a + c
    if d == 'n' or d == 'N':
        b = False
        e = a/count
        print('Sum = '+ str(a))
        print('Average = '+str(e))