#Exercise5-6
'''
student name:Bruce
ID:201810701580057
class: network 182
'''

fib = []

fib.append(0)
fib.append(1)
for i in range(2,10):
    fib.append(fib[i - 2] + fib[i - 1])

for j in fib:
    print(str(j) + ',',end='')