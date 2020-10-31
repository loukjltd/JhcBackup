#Question 6
#Josh net182 201810701580043
import random

rand = random.randint(0, 20)
print('Guess my secret number between 0 and 20 using 4 guesses')
nums = input('separated by commas: ').split(',')

for i in nums:
    if rand == int(i):
        print('You won! My secret number was: '+str(rand))
        break
else:
    print('You lost! My secret number was: '+str(rand))