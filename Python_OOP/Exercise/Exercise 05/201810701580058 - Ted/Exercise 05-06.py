#Exercise 05-06
'''
name: Ted
idnumber: 201810701580058
class: net182
'''

fib=[]
fib.append(0)
fib.append(1)
for i in range(2,10):
    fib.append(fib[i-2]+fib[i-1])
print(fib)