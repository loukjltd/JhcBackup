# Exercise 05-04
'''
Student Name: Charlie
ID: 201810101580044
Class: Network 182
'''
marks = {'Sam':90.5,'Jane':85.4,'Max':92.3,'Alice':64.5,'John':69.4}
sum = 0
for i in marks :
    sum = marks[i] + sum
marks_lenth = len(marks)
print("Sum:"+str(sum))
print("Average:"+str(sum/marks_lenth))