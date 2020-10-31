# Exercise 04-12
'''
Student Name: Faker
ID: 201810701580048
Class: Network 182
'''
for i in range(8): # do this 8 times
    for j in range(0,7-i): # go from 0 to 7-i
        print(" ", end="") # print space on same line
    for k in range(0, (2*i + 1)): # go from 0 to (2*i + 1)
        print("*", end="") # print star on same line
    print()
for i in range(7):
    for j in range(0, i + 1):
        print(' ', end='')
    for k in range(0, (2 * (6 - i) + 1)):
        print('*', end='')
    print()
