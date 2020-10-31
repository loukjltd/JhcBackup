#exercise 05-04
'''
student name: dante
student id:201810701580051
class:net 182
'''


mark = {'Sam':90.5,'Jane':85.4,'Max':92.3,'Alice':64.5,'John':69.4}
sum = 0
for values in mark:
    sum += mark[values]
print('Sum :',sum)
print('Average :',sum/len(mark))