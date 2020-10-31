'''
Class:Net182
Name:Assass
ID:201810701580040
'''
a = 3
b = 5
c = 9
def max_num(a,b,c):
    d = 0
    if a >= b:
        d = a
    else:
        d = b
    if c >= d:
        d = c
    return d
print(max_num(a,b,c))