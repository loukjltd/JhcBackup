#Exercise 13-04
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

def factorial(x):
    if x <= 0:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(5))