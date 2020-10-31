# assessment2 quertion3
'''
student name: felix
#ID: 201810701580052
#class: net182
'''
def f(x):
    if x<=0:
        return 1
    else:
        return int(x%10)*f(int(x/10))

a=int(input('inter a number :'))
print('The product of all of the digits of '+str(a)+' is '+str(f(a)))