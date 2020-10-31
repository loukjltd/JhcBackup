# Exercise 04-08
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''

sen = str(input('Please enter the sentence: '))
let = ('a', 'e', 'i', 'o', 'u')
c = 0
t = ''
for i in sen:
    if i in let:
        c += 1
        t += 'X'
    else:
        t += str(i)
print(str(t))
print('There are ' + str(c) + ' vowels in the word or sentence.')
