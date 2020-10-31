import random

rand = random.randint(0, 20)
print('Guess my secret number between 0 and 20 using 4 guesses: ')
number = input('separated by commas:')
number_list = []

for i in number.split(','):
    number_list.append(int(i))

if rand in number_list:
    print('You won! My secret number was: ',rand)
else:
    print('You lost! My secret number was: ',rand)

