# Question 4
'''
student name: Steven
ID: 201810101580037
class: network 182
'''
guess = ''
flag = True
while flag:
    guess = input('Enter a card letter: ').lower()
    if guess != 'k' and guess != 'q' and guess != 'j' and guess != 'a':
        print('Try again.')
    elif guess == 'k':
        print('King')
        flag = False
    elif guess == 'q':
        print('Queen')
        flag = False
    elif guess == 'j':
        print('Jack')
        flag = False
    elif guess == 'a':
        print('Ace')
        flag = False
