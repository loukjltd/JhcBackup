#Task6
"""
id : 201810701580049
class : Net182
name : vivi
"""
import random

rand = random.randint(0, 20)
print("Guess my secret number between 0 and 20 using 4 guesses")
user_guess = input("separated by commas: ")
user_list = user_guess.split(',')

for i in user_list:
    if int(i) == rand:
        print("You won! My secret number was: {0}".format(rand))
    else:
        print("You lost! My secret number was: {0}".format(rand))
        break