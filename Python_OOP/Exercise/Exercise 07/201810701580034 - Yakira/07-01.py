# exercise 07-01
'''
student name : Yakira
ID : 201810701580034
class : Net182
'''
a = 3
b = 5
c = 9
def max_num(a , b , c):
    if a >= b:
        largest = a
    else:
        largest = b
    if c >= a and c >= b :
        largest = c
    return largest
print(max_num(a,b,c))
