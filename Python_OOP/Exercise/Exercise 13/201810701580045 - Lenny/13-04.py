#
'''
class:net182
name:lenny
ID:201810701580045
'''
def factorial(x):
    if x <= 0:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(5))
