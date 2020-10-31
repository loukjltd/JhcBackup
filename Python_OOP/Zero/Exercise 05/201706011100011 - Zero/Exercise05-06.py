#net171 吴正博
fib=[]
fib.append(0)
fib.append(1)
for i in range(2,10):
    #fib[i]=i+fib[i-1]
    #fib.append(i+fib[i-1])
    fib.append(fib[i-2]+fib[i-1])
for i in fib:
    print(i,end=",")