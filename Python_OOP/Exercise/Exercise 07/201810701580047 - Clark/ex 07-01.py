def max_num(x, y, z):
    if x > y > z or x > z > y:
        return x
    elif y > x > z or y > z > x:
        return y
    else:
        return z


print(max_num(8, 5, 10))
