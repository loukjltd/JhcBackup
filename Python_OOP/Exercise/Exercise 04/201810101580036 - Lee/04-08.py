#exercise 04-08
'''
name:Lee
class:net182
'''

s = str(input('Please enter the sentence: '))
let = ('a', 'e', 'i', 'o', 'u')
c = 0
t = ''
for i in s:
    if i in let:
        c += 1
        t += 'X'
    else:
        t += str(i)
print(str(t))
print('There are ' + str(c) + ' vowels in the word or sentence.')