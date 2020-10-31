
# Exercise 04-09
''''
student name:Luis
ID:201810701580033
class:network 182
'''

word = str(input("Please enter a word or sentence:"))

for i in word:
    if i is 'x' :
        print("This has the letter 'x' in it",end='')
        break
else:
    print("This does not have the letter 'x' in it")