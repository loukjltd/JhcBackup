'''
Class:Net182
Name:Lester
ID:201810701580055
'''

student = {}
student['Course'] = 'IT'
student['ID'] = '2016A001'
student['Name'] = 'James'
student['Age'] = 21
print(student)
a = student['Name']
b = student['ID']
print(a + ':'+ b )
del student['Course']
for c in student:
    print(student[c])
