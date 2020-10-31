# Question 8
'''
name:Clark
class:net182
I  D:201810701580047
'''
dict1 = {'Malaysia': 38.4, 'China': 36.4, 'Australia': 22.5, 'New Zealand': 18.2}
x = 0
y = 0
for a in dict1.values():
    x += a
for b in dict1:
    print(b, ':', dict1[b])
for c in dict1.values():
    if 20 < c < 30:
        y += 1
print('Average temperature:', '{0:.2f}'.format(x/len(dict1)))
print('Maximum temperature:', '{0:.2f}'.format(max(dict1.values())))
print('Number of temperatures between 20 and 30:', y)
