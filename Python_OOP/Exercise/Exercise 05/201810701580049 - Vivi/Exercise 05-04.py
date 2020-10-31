#Exercise 05-04
'''
name:vivi
class:net182
ID：201810701580049
'''

mark = {'Sam': 90.5,'Jane': 85.4,'Max': 92.3,'Alice': 64.5,'John': 69.4}
sum = 0
for i in mark:
    sum += mark[i]
print('Sum: '+str(sum))
print('Average: '+str(sum/len(mark)))
