#Exercise 14-05
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

try:
    x = int(input("Please enter a number: "))
except ValueError as x:
    print("That was not valid number.  Try again...")
    exit(0) # stop program

try:
    f = open("C/Temp/my_numbers.txt", "r")
except IOError as f:
    print("Cannot find file")
    exit(0)  # stop program

line=f.readlines(1)
line_list=line[0].split(' ')
y=int(line_list[1])
try:
    z = x/y
except ZeroDivisionError:
    print("You cannot divide by zero")
    exit(0)  # stop program
