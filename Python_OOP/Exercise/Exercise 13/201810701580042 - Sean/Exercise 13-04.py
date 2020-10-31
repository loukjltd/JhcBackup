# Exercise 13-04
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''


def factorial(x):
    if x <= 0:
        return 1
    else:
        return x * factorial(x - 1)


print(factorial(5))
