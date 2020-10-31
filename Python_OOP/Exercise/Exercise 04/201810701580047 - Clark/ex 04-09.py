sentence = input('Please enter a word or sentence: ')
n = 0
x = 0
for a in sentence:
    x += 1
    if a == 'x' or a == 'X':
        break
    else:
        n += 1
if x == n:
    print('This does not have the letter \'x\' in it')
else:
    print('This has the letter \'x\' in it')
