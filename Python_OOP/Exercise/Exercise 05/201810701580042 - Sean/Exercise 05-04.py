# Exercise 05-04
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''

marks = {}
marks['Sam'] = 90.5
marks['Jane'] = 85.4
marks['Max'] = 92.3
marks['Alice'] = 64.5
marks['John'] = 69.4
sum = 0

for v in marks:
    sum += float(marks[v])
print('Sum: ' + str(sum))
print('Average: ' + str(sum / len(marks)))
