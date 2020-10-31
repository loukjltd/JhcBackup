'''class;net182
id address;201810701580035
name;tami'''

def factorial(x):
    if x <= 0:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(5))
