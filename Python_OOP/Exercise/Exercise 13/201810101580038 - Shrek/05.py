#exercise 13-05
'''
studentname:shrek
studentid:201810101580038
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

