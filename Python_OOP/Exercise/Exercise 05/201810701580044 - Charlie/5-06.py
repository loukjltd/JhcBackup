# Exercise 05-06
'''
Student Name: Charlie
ID: 201810101580044
Class: Network 182
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
