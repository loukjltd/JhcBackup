x = input('Enter a list of numbers separated by commas: ').split(',')
f = open('some_numbers.txt', 'w')
for a in x:
    f.write(a)
f.close()
f = open('some_numbers.txt', 'r')
y = 0
z = 0
for b in f.readline():
    print(b)
    y += int(b)
    if z < int(b):
        z = int(b)
print('Sum:', y)
print('Maximum:', z)
