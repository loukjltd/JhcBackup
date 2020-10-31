def factorial(x):
    z = 1
    for a in range(x+1):
        if x > 0:
            z *= x
            x -= 1
        else:
            break
    return z
print(factorial(5))

