#Exercise 05-04
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

Marks={'Sam':90.5,'Jane':85.4,'Max':92.3,'Alice':64.5,'John':69.4}
sum=0
for i in Marks:
    sum=sum+Marks[i]
print('Sum:'+str(sum))
print('Average:'+str(sum/len(Marks)))