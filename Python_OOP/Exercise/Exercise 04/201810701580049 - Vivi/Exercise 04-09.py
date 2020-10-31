#Exercise 04-09
'''
class:net182
name:vivi
id:201810701580049
'''

s = input("Please enter a word or sentence:")
for i in s:
    if i == "x":
        print('This has the letter \'x\' in it')
        break
else:
    print('This does not have the letter \'x\' in it')
