'''
student name:Bruce
ID:201810701580057
class: network 182
'''

import random
rand = random.randint(0,20)

print('Guess my secret number between 0 and 20 using 4 guesses')
spiltnumber = []

usercommas = input('separated by commas: ')

for i in usercommas.split():
    spiltnumber.append(int(i))

if rand in spiltnumber:
    print('You won! My secret number was: ' + str(rand))

else:
    print('You lost! My secret number was: ' + str(rand))