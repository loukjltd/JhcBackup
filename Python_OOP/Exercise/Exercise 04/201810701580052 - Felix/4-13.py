# Exercise 04-13
'''
student name: felix
#ID: 201810701580052
#class: net182
'''
num = int(input('Enter a number:'))
count = 1
choice =input('Do you want to enter another number?:')
while choice != 'n' :
    num2 = int(input('Enter a number:'))
    choice = input('Do you want to enter another number?:')
    count +=1
    s = num + num2
else:
    print('Sum = ',s)
    print('Average = ',s/count)
