#Exercise 04-08
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

word = str(input("Please enter a word or sentence: "))
z = 0
for letter in word:
    if letter in ('a','e','i','o','u'):
        print('X' , end='')
        z += 1
    else :
        print(letter , end='')
print()
print('There are '+str(z)+' vowels in the word or sentence.')
