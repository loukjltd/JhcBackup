'''
student name: Charlie
#ID: 201810701580044
#class: net182
'''
def factorial(x):
    if x <= 0:
        return 1
    else:
        return  x * factorial(x-1)

print(factorial(5))