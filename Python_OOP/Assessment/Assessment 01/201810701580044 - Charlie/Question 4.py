'''
student name: Charlie
ID: 201810701580044
class: network 182
'''
guess = ''
flag = True
while flag is True:
    guess = input('Enter a letter: ').lower()
    if guess != 'k' and guess != 'q' and guess != 'j' and guess != 'a':
        print('Try again.')
        continue
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