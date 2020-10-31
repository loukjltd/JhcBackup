x = True
y = 0
n = 0
while x:
    a = int(input('Enter a number: '))
    y += a
    n += 1
    b = input('Do you want to enter another number?: ')
    if b == 'n':
        break
    elif b == 'y':
        continue
    else:
        print('Please enter \'y\' or \'n\'')
print('Average =', y/n)