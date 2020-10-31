# exercise question 3
'''
student name: Luis
ID: 201810701580033
class: network182
'''


def f(x):
    if x<=0:
        return 1
    else:
        return int(x%10)*f(int(x/10))

num = int(input('Enter a number: '))
print('The product of all of the digits of '+str(num)+' is '+str(f(num)))
