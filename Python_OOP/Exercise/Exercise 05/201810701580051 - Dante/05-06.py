#exercise 05-06
'''
student name: dante
student id:201810701580051
class:net 182
'''




fib = []
fib.append(0)
fib.append(1)
for i in range(2,10):
    fib.append(fib[i-2]+fib[i-1])
for j in fib:
    print(str(j) + ',',end='')