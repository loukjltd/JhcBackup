# exercise 05-06
'''
student name: Eda
ID: 201810701580031
class: network182
'''


fib=[]

fib.append(0)
fib.append(1)
for i in range(2,11):
  fib.append(i+(i-1))

for j in fib:
    print(j)