# Exercise 04-13
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''

flag = True
t = 0
c = 0
while flag is True:
    n = str(input('Enter a number: '))
    t += int(n)
    c += 1
    w = str(input('Do you want to enter another number?: '))
    if w == 'y':
        flag = True
    elif w == 'n':
        flag = False
print('Sum:' + str(t))
print('Average: ' + str(t / c))
