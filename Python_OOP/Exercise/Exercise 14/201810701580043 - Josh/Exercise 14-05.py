#Exercise 14-05
#Josh net182 201810701580043

try:
    x = int(input('Please enter a number: '))
except ValueError:
    print('That was not valid number.  Try again...')
    exit(0)

try:
    f = open('./my_numbers.txt', 'r')
except IOError:
    print('Cannot find file')
    exit(0)

line = f.readline()
line_list = line.split(' ')
y = int(line_list[1])

try:
    z = x / y
except ZeroDivisionError:
    print('You cannot divide by zero')
    exit(0)