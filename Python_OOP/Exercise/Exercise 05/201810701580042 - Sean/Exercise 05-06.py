# Exercise 05-06
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''

fib = []
fib.append(0)
fib.append(1)
fib.append(fib[0] + fib[1])

for a in range(2, 9):
    fib.append(fib[a] + fib[a - 1])

for e in fib:
    print(str(e) + ', ', end='')
