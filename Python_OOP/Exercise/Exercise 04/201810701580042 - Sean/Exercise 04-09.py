# Exercise 04-09
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''

t = str(input('Please enter a word or sentence: '))
flag = False
for i in t:
    if i == 'x':
        flag = True
        print('This has the letter \'x\' in it.')
        break
if flag is False:
    print('This does not have the letter \'x\' in it.')
