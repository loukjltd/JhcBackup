# Qusetion 3
'''
Student Name: Leo
ID: 201810701580053
Class: Network 182
'''
def f(x):
    if x<=0:
        return 1
    else:
        return int(x%10)*f(int(x/10))

a=int(input('inter a number :'))
print('The product of all of the digits of '+str(a)+' is '+str(f(a)))
