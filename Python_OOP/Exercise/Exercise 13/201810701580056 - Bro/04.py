# exercise 13 04
'''
Bro
201810701580056
network 182
'''
def factorial(x):

    if x<=0:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(5))
