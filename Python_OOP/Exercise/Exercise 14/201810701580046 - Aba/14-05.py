'''
class:net182
name:Aba
ID:201810701580046
'''
try:
    x = int(input('Please enter a number: '))
except ValueError as my_ValueError:
    print('That was not valid number.Try again...')
    exit(0)
try:
    f = open('./yourname\my_numbers.txt','r')
except IOError as my_IOError:
    print('Cannot find file')
    exit(0)
a = open('./yourname\my_numbers.txt','r')
line = a.read()
line_list = line.split('')
y = int(line_list[1])
try:
    x = int(input('Please enter a number: '))
    z = x/y
except ZeroDivisionError as my_ZeroDivisionor:
    print('You cannot divide by zero')
    exit(0)