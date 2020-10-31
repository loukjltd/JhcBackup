# exercise05-06
'''
student name: Steven
ID: 201810101580037
class: network 182
'''
fib = []
fib.append(0)
fib.append(1)
c = 0
for a in range(1,10):
    c = fib[a] + fib[a-1]
    fib.append(c)
for i in fib :
    print(i,end=' ')
