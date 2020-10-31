# Exercise 05-06
'''
name:Clark
class:net182
I  D:201810701580047
'''
li = [0, 1]
for b in range(2, 10):
    x = li[-2] + li[-1]
    li.append(x)
for a in li:
    print(a, end=', ')
