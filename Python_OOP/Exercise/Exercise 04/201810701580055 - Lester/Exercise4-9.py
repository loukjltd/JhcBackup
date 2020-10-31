#Exercise 04-09
'''
Name:Lester
ID:201810701580055
Class:Net 182
'''

user=input('Please enter a word or sentence: ')
a=''
for i in user:
    if i =='x':
        a='This has the letter ‘x’ in it'
        break
    else:a='This does not have the letter ‘x’ in it'
print(a)
