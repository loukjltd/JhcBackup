a=3
b=5
c=9
def max_num(a,b,c):
    if a > b:
        largest=a
    else:
        largest=b
    if c > largest:
        largest=c
    return largest
print('Maximum number is ',max_num(a,b,c))
