'''
student name: Eden
#ID: 201810701580060
#class: net182
'''
fib = []
fib.append(0)
fib.append(1)

for i in range(2,10):
    i=fib[i-1]+fib[i-2]
    fib.append(i)

print(fib)