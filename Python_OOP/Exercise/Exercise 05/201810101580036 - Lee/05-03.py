'''
class:net182
name:Lee
ID:201810101580036
'''
student = ()
student['Name'] = 'James'
student['Age'] = 21
student['Course'] = 'IT'
student['ID'] = '2016A001'
print(student)
print(student['Name'])
print(student['ID'])
del student['Course']
for value in student:
    print(student[value])