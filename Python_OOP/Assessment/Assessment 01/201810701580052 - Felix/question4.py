w = ''
f = True
while f is True:
    w = input('Enter a letter: ').lower()
    if w != 'k' and w != 'q' and w != 'j'and w != 'a':
        print('Try again.')
    elif w == 'k' :
        print('King')
        f = False
    elif w== 'q' :
        print('queen')
        f = False
    elif w== 'a' :
        print('Ace')
        f = False
    elif w== 'j':
        print('Jack')
        f = False

