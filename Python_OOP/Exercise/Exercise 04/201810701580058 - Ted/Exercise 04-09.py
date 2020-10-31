#Exercise 04-09
'''
name: Ted
idnumber: 201810701580058
class: net182
'''

word=input('Enter a word or a sentence :')
for i in word:
    if i not in 'x':
        print('This does not have the letter \'x\' in it')
        break
    else:
        print('This has the letter \'x\' in it')
