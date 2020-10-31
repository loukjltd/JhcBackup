#exercise 13-04
'''
studentname:dante
studentid:201810701580051
class:net182
'''

def factorial(x):

    if x<=0:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(5))
