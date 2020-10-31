#exercise 05-03
'''
name:Lenny
class:net182
ID:201810701580045
'''
student = {}
student['Name'] = 'James'
student['Age'] = 21
student['Course'] = 'IT'
student['ID'] = '2016A001'
print(student)
print(student['Name'] + ':' + student['ID'])
del student['Course']
for i in student.values():
    print(i)

