#Exercise 07-01
'''
class net182
id 2018100701580049
name vivi
'''
def max_num(a,b,c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    elif a < b:
        if b > c:
            return b
        else:
            return c

print("Maximum number is " + str(max_num(3,5,9)))
