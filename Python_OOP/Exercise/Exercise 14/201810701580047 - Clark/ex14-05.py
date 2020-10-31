try:
    x = int(input("Please enter a number: "))

except ValueError:
    print("That was not valid number.  Try again...")
    exit(0) # stop program

try:
    f = open('my_numbers.txt', 'r')

except IOError:
    print("Cannot find file")
    exit(0)  # stop program


line = f.read()
line_list = line.split(' ')
y = int(line_list[1])

try:
    z = x/y
except ZeroDivisionError:
    print("You cannot divide by zero")
    exit(0)  # stop program