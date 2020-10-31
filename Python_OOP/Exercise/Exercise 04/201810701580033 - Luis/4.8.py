# Exercise 04-08
''''
student name:Luis
ID:201810701580033
class:network 182
'''

word = str(input("Please enter a word or sentence: "))
count = 0
for letter in word:
    if letter in ('a','e','i','o','u'):
        print('X' , end='')
        count += 1
    else :
        print(letter , end='')
print()
print('There are '+str(count)+' vowels in the word or sentence.')

