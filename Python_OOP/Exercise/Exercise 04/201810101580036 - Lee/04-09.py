#exercise 04-09
'''
name:Lee
class:net182
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