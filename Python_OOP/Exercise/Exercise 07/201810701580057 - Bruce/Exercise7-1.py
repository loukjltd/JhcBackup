'''
student name:Bruce
ID:201810701580057
class: network 182
'''

a = input('a= ')
b = input('b= ')
c = input('c= ')


def max_num(a,b,c):
    if a > b :
        largest = a
    else:
        largest = b
    if c > largest:
        largest = c
    return largest
print('Maximum number is ', max_num(a,b,c))


