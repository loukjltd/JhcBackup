# Qusetion6
'''
Student Name: Jax
ID: 201810701580041
Class: Net 182
'''

import random
rand=random.randint(0,20)
print('Guess my secret number between 0 and 20 using 4 guesses')
num=input('separated by commas: ')
a=[]
for i in num.split(','):
    a.append(int(i))

if rand in a:
    print('You won! My secret number was: '+str(rand))
else:
    print('You lost! My secret number was: '+str(rand))