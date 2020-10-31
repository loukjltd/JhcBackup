#Exercise 13-04
'''
class:net182
name:vivi
id:201810701580049
'''

def factorial(x):
    if x <= 1:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(5))
