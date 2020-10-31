
# Exercise 07-01
''''
student name:Luis
ID:201810701580033
class:network 182
'''



x=int(input("please enter a number"))
y=int(input("please enter a number"))
z=int(input("please enter a number"))
num=int()
def max_num(x,y,z):
    if x>y:
        if x>z:
            largest=x
        else:
            largest=z
    else:
        if y>z:
            largest=y
        else:
            largest=z
    return largest

print("max_num="+str(max_num(x,y,z)))
