line = int(input('Enter the number for the times table: '))
x = 0
for a in range(1, line + 1):
    for b in range(1, line + 1):
        x = a * b
        print(x, end='\t')
    print()
