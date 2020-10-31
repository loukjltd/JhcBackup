# Exercise 013-04
'''
name: King
idnumber: 201810701580054
class: net182
'''
def factorial(x):

    if x<=0:   # this is not Python code

        return 1
    else:
        return x*factorial(x-1)

print(factorial(5))
