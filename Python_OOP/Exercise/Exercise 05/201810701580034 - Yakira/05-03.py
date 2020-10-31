# exercise 05-03
'''
student name : Yakira
ID : 201810701580034
class : Net182
'''
student = {}
student ['Course'] = 'IT'
student ['ID'] = '2016A001'
student ['Age'] = '21'
student ['Name'] = 'James'


print(student)

print(student['Name'] + ': ' + student['ID'])
del student['Course']
for key in student:
    print (student[key])
