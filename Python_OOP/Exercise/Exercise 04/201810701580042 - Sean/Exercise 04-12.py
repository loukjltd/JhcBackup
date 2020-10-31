# Exercise 04-12
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''

for i in range(8):
    for j in range(0, 7 - i):
        print(" ", end="")

    for k in range(0, (2 * i + 1)):
        print("*", end="")
    print()

for i in range(7):
    for j in range(0, i + 1):
        print(' ', end='')

    for k in range(0, (2 * (6 - i) + 1)):
        print('*', end='')
    print()
