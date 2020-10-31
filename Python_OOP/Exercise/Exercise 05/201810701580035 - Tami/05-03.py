#exercise 05-03
'''
student name: Tami
student id:201810701580035
class:net 182
'''


student={}
student['Name'] = 'James'
student['Age'] = 21
student['Course'] = 'IT'
student['ID'] = '2016A001'
print(student)
print(student['Name'] + ':' + student['ID'])
del student['Course']
for key in student:
    print(student[key])
