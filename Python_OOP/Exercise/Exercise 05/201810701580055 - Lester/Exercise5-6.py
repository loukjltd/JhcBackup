'''
Class:Net182
Name:Lester
ID:201810701580055
'''

fib=[]
fib.append(0)
fib.append(1)
for i in range(2,10):
    fib.append(fib[i-2]+fib[i-1])
print(fib)
