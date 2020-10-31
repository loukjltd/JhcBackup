#Exercise 05-06
'''
name:vivi
class:net182
ID：201810701580049
'''

fib = []
fib.append(0)
fib.append(1)
for i in range(2, 10):
    fib.append(fib[i-1] + fib[i-2])
for i in fib:
    print(str(i)+',', end='\t')
