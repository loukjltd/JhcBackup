#Exercise 05-03
'''
name:vivi
class:net182
ID：201810701580049
'''

student = {}
student['Name'] = 'James'
student['Age'] = '21'
student['Course'] = 'IT'
student['ID'] = '2016A001'
print(student)
print(student['Name']+': '+student['ID'])
del student['Course']
for key in student:
    print(student[key])
