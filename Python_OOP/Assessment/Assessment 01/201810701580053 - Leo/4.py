'''
Student Name: leo
ID: 201810701580053
Class: Network 182
'''

A = ''
flag = True
while flag is True:
    A = input(' Please enter a letter: ').lower()
    if A != 'k' and A != 'q' and A != 'j' and A != 'a':
        print('Try again.')
        continue
    elif A == 'k':
        print('King')
        flag = False
    elif A == 'q':
        print('Queen')
        flag = False
    elif A == 'j':
        print('Jack')
        flag = False
    elif A == 'a':
        print('Ace')
        flag = False