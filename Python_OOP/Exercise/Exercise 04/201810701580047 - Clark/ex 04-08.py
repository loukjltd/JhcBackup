letter = input('enter sentence: ')
n = 0
li = ''
for a in letter:
    if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u':
        n += 1
        li += 'X'
    else:
        li += a
print(li, '\n', n)
