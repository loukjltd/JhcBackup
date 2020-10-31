# Exercise 04-02
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''

cho_n = 44
times = 5
count = 0

while count != 5:
    guess = int(input('Please guess a integer number: '))
    count += 1
    if guess != cho_n:
        print('Guess again!')
    elif guess == cho_n:
        print('Congratulation!')
        break
if count == 5:
    print('You failed!')
