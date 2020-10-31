#question6
'''
student name:Eda xiang
student ID:201810701580031
Pledge of Honour: I pledge by honour that this program is solely my own work.
'''

import random
rand = random.randint(0,20)
print("Guess my secret number between 0 and 20 using 4 guesses")
my_list = []
a = str(input("separated by commas: ").split(','))
my_list.append(a)
while a == rand:
    print("You won! My secret number was: " + str(rand))
    break
print("You lost! My secret number was: " + str(rand))