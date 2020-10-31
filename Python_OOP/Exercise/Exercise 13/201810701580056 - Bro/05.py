# exercise 13 05
'''
Bro
201810701580056
network 182
'''
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n=20
for a in range(n):
    print(fibonacci(a),end=',')

