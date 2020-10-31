#Question 4
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

letter=input('The letter of a play card').lower()
print('Enter a letter:'+str(letter))
while letter=='K'or letter=="Q" or letter=="J" or letter=="A":
    if letter=="K":
        print('King')
    elif letter=="Q":
        print('Queen')
    elif letter=="J":
        print('Jack')
    else:
        print('Ace')
    break
print('Try again.')
