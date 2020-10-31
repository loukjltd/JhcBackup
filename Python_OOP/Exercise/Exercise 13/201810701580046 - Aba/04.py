#exercise 13-04
'''
studentname:Aba
studentid:201810701580046
class:net182
'''

def factorial(x):

    if x<=0:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(5))
