# exercise 14-05
'''
student name: Luis
ID: 201810701580033
class: network182
'''

try:
    x = int(input("Please enter a number: "))
except ValueError as my_err:
    print( "That was not valid number.  Try again...")
    exit(0) # stop program

try:
    f=open("./my_numbers.txt")
except IOError as my_err:
    print("Cannot find file")
    exit(0)  # stop program

line_list=[]
line=open('./my_numbers.txt','r')
for line in f.readlines():
      split_line = line.split(",")
      line_list.append(split_line)
      y= int(split_line[1])

try:
    z = x/y
except ZeroDivisionError as my_err:
    print( "You cannot divide by zero")
    exit(0)  # stop program
