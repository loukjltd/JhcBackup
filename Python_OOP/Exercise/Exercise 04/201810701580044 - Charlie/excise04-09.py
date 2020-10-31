# Exercise 04-09
'''
Student Name: Charlie
ID: 201810101580044
Class: Network 182
'''
message = str(input('please enter a word or sentence:'))
for i in message:
    if i == 'x':
        print('This has the letter \'x\' in it')
        break
else:
    print('This dose not has the letter \'x\' in it')
