#Exercise 04-09
'''
name: Jax
idnumber: 201810701580041
class: net182
'''

word=input('Enter a word or a sentence :')
for i in word:
    if i not in 'x':
        print('This does not have the letter \'x\' in it')
        break
    else:
        print('This has the letter \'x\' in it')
