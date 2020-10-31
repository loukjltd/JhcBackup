# exercise 04-08
'''
name:Lenny
class:net182
ID:201810701580045
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