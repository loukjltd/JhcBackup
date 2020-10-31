# exercise 13-04
'''
student name: Eda
ID: 201810701580031
class: network182
'''
def factorial(x):
    if x <= 0:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(5))