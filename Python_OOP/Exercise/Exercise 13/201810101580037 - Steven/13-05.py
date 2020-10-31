# exercise13-05
'''
student name: Steven
ID: 201810101580037
class: network 182
'''
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return  fibonacci(n-1) + fibonacci(n-2)

n = 20
for a in range(n):
    print(fibonacci(a),end=",")
