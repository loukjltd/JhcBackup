# exercise 05-06
'''
student name : Yakira
ID : 201810701580034
class : Net182
'''
fib = []
fib.append(0)
fib.append(1)
x = 0
for b in range(2,10):
    x = fib[-2] + fib[-1]
    fib.append(x)
print(fib)


