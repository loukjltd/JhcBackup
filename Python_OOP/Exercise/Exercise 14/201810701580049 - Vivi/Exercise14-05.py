#Exercise 14-05
"""
class:net182
name:vivi
id:201810701580049
"""
global file,x

try:
    x = int(input('Please enter a number: '))
except ValueError:
    print('That was not valid number.  Try again...')
    exit(0)

try:
    file = open('my_numbers.txt', 'r')
except IOError:
    print('Cannot find file')
    exit(0)

line = file.readline()
line_list = line.split(' ')
y = int(line_list[1])

try:
    z = x / y
except ZeroDivisionError:
    print('You cannot divide by zero')
    exit(0)