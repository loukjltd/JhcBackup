'''
Class:Net182
Name:Assass
ID:201810701580040
'''
import random
r = random.randint(0, 20)
print('Guess my secret number between 0 and 20 using 4 guesses')
l = input('separated by commas: ').split(',')
if r in l:
    print('You won! My secret number was: ' + str(r))
else:
    print('You lost! My secret number was: ' + str(r))