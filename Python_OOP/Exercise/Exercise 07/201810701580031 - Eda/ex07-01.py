# exercise 07-01
'''
student name: Eda
ID: 201810701580031
class: network182
'''

x = 3
y = 5
z = 9
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

print('Maximum number is：' + str(max_num(x,y,z)))





