#Exercise 13-05
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = 20
for i in range (0,n-1):
    print(fibonacci(i))