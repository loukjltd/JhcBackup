# Question 6
'''
name:Clark
class:net182
I  D:201810701580047
'''
import random
rand = random.randint(0, 20)
x = 0
print('Guess my secret number between 0 and 20 using 4 guesses')
guess = input('separated by commas: ').split(',')
if len(guess) <= 4:
    for a in guess:
        x += 1
        if a == rand:
            print('You won! My secret number was:', rand)
            break
        if x == 4 and a != rand:
            print('You lost! My secret number was:', rand)
else:
    print('you just guess 4 number')
