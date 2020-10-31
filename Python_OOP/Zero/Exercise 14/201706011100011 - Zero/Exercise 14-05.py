# net171-ZhaoYinting

try:
    x = int(input("Please enter a number: "))
except ValueError as my_err:
    print("That was not a number. Try again...")

try:
    f = open("my_numbers.txt", "r")
except IOError as my_err:
    print("Cannot find file")

f = open("my_numbers.txt", "r")
line = f.read()
line_list = line.split(" ")
y = int(line_list[1])


try:
    x = int(input("Please enter a number: "))
    z = x/y
except ValueError as my_err:
    print("That was not a number. Try again...")
except ZeroDivisionError as my_err:
    print("You cannot divide by zero")
