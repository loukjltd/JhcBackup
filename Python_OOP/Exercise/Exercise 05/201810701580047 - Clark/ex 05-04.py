# Exercise 05-04
'''
name:Clark
class:net182
I  D:201810701580047
'''
dict = {'Sam': 90.5, 'Jane': 85.4, 'Max': 92.3, 'Alice': 64.5, 'John': 69.4}
x = 0
y = 0
for a in dict:
   x += dict[a]
   y += 1
print('Sum:', x)
print('Average:', x/y)
