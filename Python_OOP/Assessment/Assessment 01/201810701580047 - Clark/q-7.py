# Question 7
'''
name:Clark
class:net182
I  D:201810701580047
'''
fl = input('Enter the first line of numbers separated by commas: ').split(',')
sl = input('Enter the second line of numbers separated by commas:').split(',')
x = 0
for a in fl:
    for b in sl:
        if a == b:
            x += 1
print('There are ' + str(x) + ' numbers that are in both lists')
