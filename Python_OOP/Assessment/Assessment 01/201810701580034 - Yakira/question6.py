'''
student name: Yakira
ID: 201810701580034
Pledge of Honour: I pledge by honour that this program is solely my own work.
'''
import random
rand = random.randint(0, 20)
print('Guess my secret number between 0 and 20 using 4 guesses separated by commas:')
num = str(input('separated by commas: ')).split(",")
x = 0
for a in num :
    x += 1
    if int(a) == rand:
        print("You won! My secret number was:",rand)
        break
    elif x == 4 and int(a) != rand :
        print ("You lost! My secret number was:",rand)




