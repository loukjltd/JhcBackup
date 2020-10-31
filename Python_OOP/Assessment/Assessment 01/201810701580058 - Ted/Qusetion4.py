# Qusetion4
'''
Student Name: Ted
ID: 201810701580058
Class: Net 182
'''

letter=input('enter a card letter:').lower()
a=True
while a==True:
    if letter!='k' and letter!='q' and letter!='a' and letter!='j':
        print('Try agian')
        letter = input('enter a card letter:').lower()
        continue
    elif letter=='k':
        print('King')
        a=False
    elif letter=='q':
        print('Queen')
        a = False
    elif letter=='j':
        print('Jack')
        a = False
    elif letter=='a':
        print('Ace')
        a = False
