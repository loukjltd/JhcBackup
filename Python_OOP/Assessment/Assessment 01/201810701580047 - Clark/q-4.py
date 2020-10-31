# Question 4
'''
name:Clark
class:net182
I  D:201810701580047
'''
x = True
while x:
    et = input('Enter a card letter: ').lower()
    if et == 'k':
        print('King')
        break
    elif et == 'q':
        print('Queen')
        break
    elif et == 'j':
        print('Jack')
        break
    elif et == 'a':
        print('Ace')
        break
    else:
        print('Try again')
