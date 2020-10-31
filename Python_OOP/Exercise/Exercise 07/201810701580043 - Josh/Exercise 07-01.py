#Exercise 07-01
#Josh net182 201810701580043

def max_num(a,b,c):
    max1 = 0
    if a > b:
        max1 = a
    else:
        max1 = b
    if c > max1:
        max1 = c
    return max1

print(max_num(1,2,3))
print(max_num(6,7,3))
print(max_num(11,9,3))
