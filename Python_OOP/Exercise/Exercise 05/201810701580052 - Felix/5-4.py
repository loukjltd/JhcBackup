# Exercise 05-04
'''
student name: felix
#ID: 201810701580052
#class: net182
'''
marks ={'Sam':90.5,'Jane':85.4,'Max':92.3,'Alice':64.5,'John':69.4}
sum = 0
for i in marks:
    sum = sum + marks[i]
print('Sum: ',sum)
print('Average: ',sum/len(marks))