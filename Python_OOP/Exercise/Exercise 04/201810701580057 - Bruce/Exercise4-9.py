#Exercise4-9
'''
student name:Bruce
ID:201810701580057
class: network 182
'''

word = input('Please enter a word or sentence: ')

for i in word:
    if i == 'x':
        print('This has the letter' + "'x'" + 'in it')
        break
else:
    print('This does not have the letter' + "'x'" + 'in it')