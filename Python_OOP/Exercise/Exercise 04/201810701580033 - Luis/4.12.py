



# Exercise 04-12
''''
student name:Luis
ID:201810701580033
class:network 182
'''

a=int(input('please enter a number' ))
for i in range (a):
    for j in (0,7-i):
        print (' ',end='')
    for k in range (0,(2*i+1)):
        print(('*'),end='')
    print()
for i in range(a):
    for j in range(i):#(1,rows-i)
        print(" ", end="")
        j += 1
    for k in range(2 * (7 - i) + 1):
        print("*", end="")
    print()