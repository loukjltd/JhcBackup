'''
Class:Net182
Name:Assass
ID:201810701580040
'''
def get_sum(x):
    if len(x)<=0:
        return 1
    else:
        z=x[1:]
        return x[0] * get_sum(z)
l=[1.2, 2.0, 3.5, 5.3]
c=get_sum(l)
print(c)