# exercise13-04
'''
student name: Steven
ID: 201810101580037
class: network 182
'''
def factorial(x):
    if x <= 0:
        return 1
    else:
        return  x * factorial(x-1)

print(factorial(5))
