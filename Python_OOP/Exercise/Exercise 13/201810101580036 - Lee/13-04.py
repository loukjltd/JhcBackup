'''
name:Lee
class:net182
ID:201810101580036
'''
def factorial(x):
    if x <= 0:
        return 1
    else:
        return x * factorial(x - 1)
print(factorial(5))