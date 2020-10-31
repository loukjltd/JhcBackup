#it171 ZERO

def max(x,y,z):
    if x>y:
        largest=x
    else:
        largest=y
    if z>largest:
        largest=z
    return largest
print(max(3,5,9))