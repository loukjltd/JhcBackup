# exercise 04 08
'''
Bro
201810701580056
network 182
'''
sen = str(input('Please enter the sentence: '))
let = ('a', 'e', 'i', 'o', 'u')
count = 0
t = ''
for i in sen:
    if i in let:
        count += 1
        t += 'X'
    else:
        t += str(i)
print(str(t))
print('There are ' + str(count) + ' vowels in the word or sentence.')

