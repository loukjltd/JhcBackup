# exercise 14-05
'''
student name: Eda
ID: 201810701580031
class: network182
'''

try:
    x = int(input("Please enter a number: "))
except ValueError as x:
    print("That was not valid number.  Try again...")
    exit(0)

try:
    f = open("./my_numbers.txt","r")
except IOError as f:
    print("Cannot find file")
    exit(0)

line = f.readlines(1)
line_list = line[0].split(" ")
y = int(line_list[1])
try:
    z = x / y
except ZeroDivisionError:
    print("You cannot divide by zero")
    exit(0)