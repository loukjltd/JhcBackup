# exercise 04-09
'''
name:Lenny
class:net182
ID:201810701580045
'''
sentence = input('Please enter a word or sentence:')
for i in sentence:
    if i == 'x':
        print('This has the letter ' + str('x') + ' in it')
        break
else:
    print('This does not have the letter ' + str('x') + ' in it')
