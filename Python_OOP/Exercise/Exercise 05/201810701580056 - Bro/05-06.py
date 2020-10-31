# exercise 05 06
'''
Bro
201810701580056
network 182
'''
fib = []
fib.append(0)
fib.append(1)
for i in range(2,9):
    fib.append(fib[i-2]+fib[i-1])
for j in fib:
    print(str(j) + ',',end='')