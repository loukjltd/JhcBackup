#exercise 13-05
'''
studentname:dante
studentid:201810701580051
class:net182
'''

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n=20
for a in range(n):
    print(fibonacci(a),end=',')

