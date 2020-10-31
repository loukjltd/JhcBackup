# exercise 04-08
'''
student name : Yakira
ID : 201810701580034
class : Net182
'''
word = str(input("Please enter a word or sentence: "))
b = 0
for letter in word:
    if letter in ('a','e','i','o','u'):
        print('X' , end='')
        b += 1
    else :
        print(letter , end='')
print()
print('There are '+str(b)+' vowels in the word or sentence.')


