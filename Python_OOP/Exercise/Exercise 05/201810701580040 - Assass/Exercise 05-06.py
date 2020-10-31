#Exercise 05-06
'''
name: Assass
idnumber: 201810701580040
class: network 182
'''
fib=[]
fib.append(0)
fib.append(1)
print(fib)
for i in range(2,10):
    fib.append(fib[i-2]+fib[i-1])

for i in range(0,10):
    print(str(fib[i])+',',end='')