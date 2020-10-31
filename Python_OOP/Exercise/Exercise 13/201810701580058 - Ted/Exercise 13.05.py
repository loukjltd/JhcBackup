# Exercise 013-05
'''
Student Name: Ted
ID: 201810701580058
Class: Network 182
'''
def fibonacci(n):

    if n<=1:
        return n

    else:
        return fibonacci(n-1)+fibonacci(n-2)

n=20

for i in range(n):
    print(fibonacci(i),end=',')