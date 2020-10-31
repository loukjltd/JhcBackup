# exercise 05-03
'''
student name: Eda
ID: 201810701580031
class: network182
'''


student = {}
student['Name'] = 'James'
student['Age'] = 21
student['Course'] = 'IT'
student['ID'] = '2016A001'
print(student)

print(student['Name'] + ' : ' + student['ID'])

del student['Course']
for i in student:
    print(student[i])