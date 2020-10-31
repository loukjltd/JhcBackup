#exercise 13-04
'''
studentname:shrek
studentid:201810101580038
class:net182
'''

def factorial(x):

    if x<=0:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(5))
