def max_num(x,y,z):
    if x > y:
        largest = x
    else:
        largest = y
    if z > largest:
        largest = z
    return largest
x =3
y =5
z =9
print('Maximum number is ' + str(max_num(x,y,z)))
