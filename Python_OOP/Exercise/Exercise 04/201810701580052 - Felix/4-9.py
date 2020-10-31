# Exercise 04-09
'''
student name: felix
#ID: 201810701580052
#class: net182
'''
word = str(input('please enter a word or sentence:'))
for i in word:
    if i == 'x':
        print("This has the letter 'x' in it")
        break
else:
    print( "This does not have the letter 'x' in it")
