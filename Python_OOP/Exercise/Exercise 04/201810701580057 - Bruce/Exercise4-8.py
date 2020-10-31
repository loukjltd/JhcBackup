#Exercise4-8
'''
student name:Bruce
ID:201810701580057
class: network 182
'''
count = 0
word = input('Enter a word or sentence: ')
for letter in word:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        print('x',end='')
        count += 1
    else:
        print(letter,end='')
print( )
print('There are ' + str(count) + ' vowels in the word or sentence')
