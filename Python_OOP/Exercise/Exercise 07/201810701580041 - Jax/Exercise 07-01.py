# Exercise 07-01
'''
Student Name: Jax
ID: 201810701580041
Class: Net 182
'''

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
x=input('enter the first number:')
y=input('enter the second number:')
z=input('enter the thied number:')
a=max_num(x,y,z)
print(a)