#Exercise 04-08
'''
name: Jax
idnumber: 201810701580041
class: net182
'''

word=input('Enter a word or sentence: ')
count=0
for i in word:
    if i in ('a','i','e','o','u'):
        i='X'
        count += 1
    print(i, end='')

print()
print('There are '+str(count)+' vowels in the word or sentence.')
