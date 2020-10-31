#exercise 07-01
'''
student name:shrek
student id:201810101580038
class:net182
'''


x=input('number1: ')
y=input('number2:  ')
z=input('number3: ')


def max_num(x,y,z):
    if x > y:
        largest = x
    else:
        largest = y
    if z > largest:
        largest = z
    return largest
print('Maximum number is ',max_num(x,y,z))