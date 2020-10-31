# Exercise 13-05
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(20):
    print(fibonacci(i), end=', ')
