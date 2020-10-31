#Exercise 07-01
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

a = 3
b = 5
c = 9
def max_num(x,y,z):
    if x > y:
        if x > z:
            largest = x
        else:
            largest = z
    else:
        if y > z:
            largest = y
        else:
            largest = z
    return largest

print("The largest number is:"+ str(max_num(x,y,z)))


