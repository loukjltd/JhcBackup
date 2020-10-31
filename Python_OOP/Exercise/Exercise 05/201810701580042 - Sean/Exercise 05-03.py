# Exercise 05-03
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''

student = {}
student['Name'] = 'James'
student['Age'] = 21
student['Course'] = 'IT'
student['ID'] = '2016A001'
print(student)

print(str(student['Name']) + ': ' + str(student['ID']))

del student['Course']

for key in student:
    print(student[key])
