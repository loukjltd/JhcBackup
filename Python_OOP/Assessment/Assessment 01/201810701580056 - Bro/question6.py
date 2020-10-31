# question6
'''
Bro
201810701580056
network 182
'''
import random
rand = random.randint(0, 20)
guess_number = []
print('Guess my secret number between 0 and 20 using 4 guesses')
guess = input('separated by commas: ')

for i in guess.split(','):
    guess_number.append(int(i))

if rand in guess_number:
    print('You won! My secret number was: ' + str(rand))
else:
    print('You lost! My secret number was: ' + str(rand))