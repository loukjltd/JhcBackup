#Exercise 13-05
'''
class:net182
name:vivi
id:201810701580049
'''

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 20
for i in range(0, n):
    print(fibonacci(i))
