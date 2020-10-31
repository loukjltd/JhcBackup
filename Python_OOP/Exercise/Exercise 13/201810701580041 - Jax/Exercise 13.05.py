# Exercise 013-05
'''
Student Name: Jax
ID: 201810701580041
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