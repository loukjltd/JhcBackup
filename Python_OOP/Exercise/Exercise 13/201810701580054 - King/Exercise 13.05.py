# Exercise 013-05
'''
name: King
idnumber: 201810701580054
class: net182
'''
def fibonacci(n):

    if n<=1:
        return n

    else:
        return fibonacci(n-1)+fibonacci(n-2)

n=20

for i in range(n):
    print(fibonacci(i),end=',')