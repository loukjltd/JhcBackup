'''
Student name: Luis Zhou
Student ID: 2018100701580033
Pledge of Honour: I pledge by honour that this program is solely my own work.
'''

card=input(' the letter of a play card').lower()
print('Enter a card letter:'+str(card))
while card=='k'or card=="q" or card=="j" or card=="a":
    if card=="k":
        print('King')
    elif card=="q":
        print('Queen')
    elif card=="j":
        print('Jack')
    else:
        print('Ace')
    break
print('Try again')
