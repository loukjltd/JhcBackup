# exercise05-04
'''
student name: Steven
ID: 201810101580037
class: network 182
'''
marks = {'Sam':90.5,'Jane':85.4,'Max':92.3,'Alice':64.5,'John':69.4}
sum = 0
for i in marks :
    sum = marks[i] + sum
marks_lenth = len(marks)
print("Sum:"+str(sum))
print("Average:"+str(sum/marks_lenth))
