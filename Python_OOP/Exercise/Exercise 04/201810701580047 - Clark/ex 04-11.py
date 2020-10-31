n = 0
print('M  ', 'T  ', 'W  ', 'T  ', 'F  ', 'S  ', 'SU')
for a in range(1, 32):
    print(a, end='\t')
    n += 1
    if n >= 7:
        print('\n')
        n = 0

