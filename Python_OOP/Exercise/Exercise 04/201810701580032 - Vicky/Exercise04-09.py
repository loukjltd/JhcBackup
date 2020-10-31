#Exercise 04-09
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

user = str(input("Please enter a word or sentence:"))

for i in user:
    if i is 'x' :
        print("This has the letter 'x' in it",end='')
        break
else:
    print("This does not have the letter 'x' in it")