# exercise 13-05
'''
student name: Yakira
ID: 201810701580034
class: network182
'''
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = 20
for i in range (0,n-1):
    print(fibonacci(i))

