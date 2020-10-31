'''
student name:Bruce
ID:201810701580057
class: network 182
'''

playcard = ''
name = True
while name is True:
    playcard = input('Enter a letter: ').lower()
    if playcard != 'k' and playcard != 'q' and playcard != 'j' and playcard != 'a':
        print('Try again')
        continue
    elif playcard == 'k':
        print('King')
        name = False
    elif playcard == 'q':
        print('Queen')
        name = False
    elif playcard == 'j':
        print('Jake')
        name = False
    elif playcard == 'a':
        print('Ace')
        name = False