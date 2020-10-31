# exercise 14-05
'''
student name: Yakira
ID: 201810701580034
class: network182
'''
try:
    x = int(input("Please enter a number: "))
except ValueError as my_err:
    print('That was not valid number. Try again...')
    exit(0)

try:
    f = open('my_numbers.txt','r')
except IOError as my_err:
    print('Cannot find file')
    exit(0)

line = f.readlines()
line_list = []
for i in f.readlines():
    line_list.append(i.split(''))
y = int(line_list[1])

try:
    z = x/y
except ZeroDivisionError as my_err:
    print('You cannot divide by zero')
    exit(0)