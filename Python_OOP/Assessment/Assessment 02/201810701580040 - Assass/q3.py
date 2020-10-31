'''
class:net182
name:Assass
id:201810710580040
'''
def f(x):
    if x<=0:
        return 1
    else:
        return int(x%10)*f(int(x/10))

a=int(input('Enter a number: '))
print('The product of all of the digits of '+str(a)+' is '+str(f(a)))